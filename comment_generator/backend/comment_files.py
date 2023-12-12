import os
from pathlib import Path
import shutil
from typing import Callable

import comment_generator.backend.code_commentor_tool as gpt_tool
from comment_generator.configuration.log_factory import logger
import comment_generator.backend.together_ai_streaming as opensource_tool
import comment_generator.backend.extract_code_service as extract_code
import comment_generator.cli_services.pylint_services as pylint_services
import comment_generator.cli_services.format_service as format_service

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
                code_extracted = get_output(code_commentor_func, code)
                if code_extracted == "":
                    print("in except")
                    code_extracted = get_output(code_commentor_func, code)
                    print(code_extracted)
                    if code_extracted == "":
                        with open(f"{name}", mode="w") as f:
                            if folder.endswith(".py"):
                                f.write("## Some error occured in putting comments")
                            else:
                                f.write("// Some error occured in putting comments")
                            f.write("\n")
                            f.write(code)
                    else:
                        final_code(name, code_extracted)

                else:
                    final_code(name, code_extracted)


def final_code(name, code_extracted):
    code_formatted = format_service.format_file(Path(name), code_extracted)
    pylint_services.lint_code(Path(name), code_formatted)   
    with open(f"{name}", mode="w") as f:
        f.write(code_formatted)


def get_output(code_commentor_func, code):
    output = code_commentor_func(code)
    code_extracted = extract_code.extract_code(output)
    code_extracted = code_extracted.lstrip(" ")
    return code_extracted


def comment_python_files_gpt(source_folder, destination_folder):
    process_python_files(
        source_folder, destination_folder, lambda code: gpt_tool.code_commentor(code)
    )


def comment_python_files_opensource(source_folder, destination_folder):
    process_python_files(
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
