from pathlib import Path
from black import format_str
from black import Mode


def format_file(file: Path, code: str) -> str:
    assert code is not None
    try:
        formatted = format_str(code, mode=Mode())
        return formatted
    except Exception as e:
        file_name = file.name
        temp_file = file.parent / f"{file_name}_black.txt"
        temp_file.write_text(str(e), encoding="utf-8")
        return code


if __name__ == "__main__":
    file = Path(
        r"C:\Users\Sayalee\Projects\commented_projects\image_generator_bot\image_generator_bot\backend\download_img.py"
    )
    f = open(file, "r")
    code = f.read()
    print(format_file(file, code))
