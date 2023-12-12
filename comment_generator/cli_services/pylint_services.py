import datetime
from pathlib import Path

from pylint.lint.run import Run
from comment_generator.config_toml import cfg


def lint_code(file, code):
    parent = file.parent
    file_name = file.name
    output_file = parent / f"{file_name}_lint.txt"
    temp_file = Path("/tmp/temp.py")
    temp_file.write_text(code, encoding="utf-8")
    Run([f"--output={output_file}", temp_file.as_posix()], exit=False)
    return output_file


if __name__ == "__main__":
    import asyncio

    model = "WizardLM/WizardCoder-15B-V1.0"
    question = "Generate python code to display numbers from 1 to 30"
    code = """"
    ```python
for i in range(1, 31):
    print(i)
```

This code uses a for loop and the `range()` function to iterate over the numbers from 1 to 30 (inclusive) and print each number on a new line. 
The `range()` function generates a sequence of numbers starting from the first argument (1) and ending at the second argument (31), incrementing by 1 each time.
    """
    output_file = asyncio.run(lint_code(code, question, model))
    assert output_file is not None
    assert output_file.exists()