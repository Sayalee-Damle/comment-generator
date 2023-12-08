import comment_generator.backend.comment_files as comment
from comment_generator.configuration.config import cfg
import pathlib


def key_model(model):
    api_key = input("Give API key or put it in the .env file: ")
    if api_key == "":
        print("Please don't forget to put the key in the .env file")
    else:
        if model == "chat-gpt":
            cfg.openai_api_key = api_key
        else:
            cfg.together_api_key = api_key


src_file_path = input("Enter code directory to be commented: ")
src_file_path = pathlib.Path(
    src_file_path.strip('"')
).as_posix()  # pathlib.Path(r"C:\Users\Sayalee\Projects\langchain\image_generator_bot").as_posix()
dest_file_path = input(
    "Where do you want the commented code directory to be? please give the path of the root folder: "
)
dest_file_path = pathlib.Path(dest_file_path.strip('"')).as_posix()
# pathlib.Path(r"C:\Users\Sayalee\Projects\commented_projects\image_generator_bot").as_posix()

models = "\n".join(cfg.updated_model_list)
model_to_use = input(models + "\nchat-gpt" + "\nchoose the model you want to use: ")

if model_to_use == "":
    model_to_use = "togethercomputer/llama-2-70b-chat"

if model_to_use.lower() == "chat-gpt":
    key_model("chat-gpt")
    comment.comment_python_files_gpt(src_file_path, dest_file_path)
else:
    print(
        "Use TOGETHERAI for this, create an account and generate a key (https://docs.together.ai/docs/get-started)"
    )
    key_model("together-ai")
    comment.comment_python_files_opensource(src_file_path, dest_file_path, model_to_use)
