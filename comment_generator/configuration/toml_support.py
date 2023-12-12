from pathlib import Path
import tomli
from comment_generator.configuration.config import cfg


def read_toml(file: Path) -> dict:
    with open(file, "rb") as f:
        return tomli.load(f)


def read_prompts_toml() -> dict:
    return read_toml("./prompts.toml")


prompts = read_prompts_toml()

if __name__ == "__main__":
    print(prompts)
