from cx_Freeze import setup, Executable






__version__ = '1.0.0'




packages = [
"openai",
"pydantic",
"transformers",
"sentencepiece",
"ninja",
"packaging",
"torch" ,
"tomli" ,
"together",
#"pylint",
"openpyxl",
"yapf",
"click",
]

exe = Executable(
    script=".\comment_generator\main.py",
    base="Console",
    target_name="comment_generator.exe",
)

setup(
    name='comment_generator',
    description='generates comments for python code',
    version=__version__,
    executables=[exe],
    options = {'build_exe': {'packages': packages}}
)

