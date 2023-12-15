from openai import AsyncOpenAI
import toml
from pathlib import Path
from dotenv import load_dotenv
import os
import json

config = toml.load("./config.toml")
load_dotenv()


class Config:
    openai_api_key = os.getenv("OPENAI_API_KEY")
    together_api_key = os.getenv("TOGETHER_API_KEY")

    model_gpt=config["env"]["model_name"]
    temperature=config["env"]["temperature"]
    request_timeout=config["env"]["ui_timeout"]
    cache=config["env"]["llm_cache"]
    streaming=True

    code_output = Path(config["env"]["code_output"])
    if not code_output.exists():
        code_output.mkdir(exist_ok=True, parents=True)

    code_comment = Path(config["env"]["code_comment"])
    if not code_comment.exists():
        code_comment.mkdir(exist_ok=True, parents=True)

    window_size = json.loads(config["env"]["window_size"])

    verbose_llm = config["env"]["verbose_llm"]

    open_ai_client = AsyncOpenAI(
        api_key=openai_api_key,
    )
    
cfg = Config()


if __name__ == "__main__":
    print(config)
    print(cfg.together_api_key)
    print(cfg.window_size)
