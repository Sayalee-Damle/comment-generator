import os
from pathlib import Path
import shutil
from typing import Callable
import asyncio

import comment_generator.backend.gpt_code_comment as gpt_tool
from comment_generator.configuration.log_factory import logger
import comment_generator.backend.together_ai_streaming as opensource_tool
import comment_generator.cli_services.extract_code_service as extract_code
import comment_generator.cli_services.pylint_services as pylint_services
#import comment_generator.cli_services.format_service as format_service


def process_python_files(
    source_folder: str, destination_folder: str, code_commentor_func: Callable
):
    source_dir_path = os.path.realpath(source_folder)
    dest_dir_path = os.path.realpath(destination_folder)
    shutil.copytree(
        source_dir_path,
        dest_dir_path,
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns("*.git"),
    )
    # print(dest_dir_path)
    for root, dirs, files in os.walk(dest_dir_path):
        for folder in files:
            if folder.endswith(".py") or folder.endswith(".java"):
                name = root + "\\" + str(folder)
                print(name)
                f = open(name, "r")
                code = f.read()
                if code == "":
                    continue
                # print(code)
                try:
                    code_extracted = get_output(code_commentor_func, code)
                    if code_extracted == "":
                        code_extracted = handle_failure(code_commentor_func, name, code)
                except:
                    logger.exception(f"Could not process {name}")

                else:
                    final_code(name, code_extracted)


def handle_failure(code_commentor_func: Callable, name: str, code: str) -> str:
    print("in except")
    code_extracted = get_output(code_commentor_func, code)
    print(code_extracted)
    if code_extracted == "":
        with open(f"{name}", mode="w") as f:
            f.write("## Some error occured in putting comments")

            f.write("\n")
            f.write(code)
    else:
        final_code(name, code_extracted)
    return code_extracted


def final_code(name: str, code_extracted: str):
    #code_formatted = format_service.format_file(Path(name), code_extracted)
    pylint_services.lint_code(Path(name), code_extracted)
    with open(f"{name}", mode="w") as f:
        f.write(code_extracted)


def get_output(code_commentor_func: Callable, code: str) -> str:
    output = code_commentor_func(code)
    code_extracted = extract_code.extract_code(output)
    code_extracted = code_extracted.lstrip(" ")
    return code_extracted


def comment_python_files_gpt(source_folder: str, destination_folder: str):
    process_python_files(
        source_folder, destination_folder, lambda code: asyncio.run(gpt_tool.code_commentor(code))
    )


def comment_python_files_opensource(source_folder: str, destination_folder: str, model: str):
    process_python_files(
        source_folder,
        destination_folder,
        lambda code: opensource_tool.comment_code_opensource(code,model),
    )


### Single File computation


def comment_single_python_file_process(
    source_folder, destination_folder, code_commentor_func: Callable
):
    source_dir_path = os.path.realpath(source_folder)
    dest_dir_path = os.path.realpath(destination_folder)
    shutil.copyfile(
        source_dir_path,
        dest_dir_path,
    )

    f = open(dest_dir_path, "r")
    code = f.read()
    if code == "":
        return
    try:
        code_extracted = get_output(code_commentor_func, code)
        if code_extracted == "":
            code_extracted = handle_failure(code_commentor_func, dest_dir_path, code)
    except:
        logger.exception(f"Could not process {dest_dir_path}")

    else:
        final_code(dest_dir_path, code_extracted)


def comment_single_python_file_gpt(source_folder, destination_folder):
    comment_single_python_file_process(
        source_folder, destination_folder, lambda code: gpt_tool.code_commentor(code)
    )


def comment_single_python_file_opensource(source_folder, destination_folder):
    comment_single_python_file_process(
        source_folder,
        destination_folder,
        lambda code: opensource_tool.comment_code_opensource(code),
    )


if __name__ == "__main__":
    src_file_path = input("Enter code directory to be commented: ")
    dest_file_path = input(
        "Where do you want the commented code directory to be? please give the path of the root folder: "
    )
    # print(comment_python_files_opensource(file_path))
    print(comment_python_files_opensource(src_file_path, dest_file_path))
#   C:\Users\Sayalee\Projects\langchain\image_generator_bot
#   C:\Users\Sayalee\Projects\commented_projects\image_generator_bot
