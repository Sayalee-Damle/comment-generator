# Comment Generator

## Description

A simple command line tool that you can use to add comments to a Python code base.
It uses AI to generate comments for the code given in.
It provides this functionality using 2 different AI model options:
- ChatGPT
- Llama-2-70b-chat using TogetherAI 
If the model is unable to put in the comments, the original code is put in with a comment indicating the same.
The tool does not make changes inplace, it makes a copy of the code base into a folder given by the user. 
This is done to ensure that the original code stays intact even if the model gives out some abnormality.
Programming language used: Python
Command-Line Interface Python Package - Click

## Installation Instructions

Please install [Conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html) first and then run the following commands:

```
conda create -n comment_generator python=3.11
conda activate comment_generator
pip install poetry
poetry install
```

## Environment

The project needs a `.env` file in its root folder
To Check the format of the `.env` file, please take a look at the `.env_local` file. Put the parameters in and copy paste it in the `.env` file.

Or you need to have the following environment variables defined:
```
TOGETHER_API_KEY = #togetherAI Key
TEMPERATURE = 0.1
MAX_TOKENS = 3000
TOP_K = 1
PROJECT_ROOT = #project path
UI_TIMEOUT = 300
OPENAI_MODEL = gpt-4-1106-preview
OPENAI_API_KEY= #openAI key
CHUNK_SIZE = 1000
REQUEST_TIMEOUT = 300
LLM_CACHE = False
VERBOSE_LLM = True
TOKEN_LIMIT = 13000
```

## How to run the application

This is the main entry point of the application

```
python .\comment_generator\main.py
```

For help about the command line parameters and information, just type:

```
python .\comment_generator\main.py --help
```

## Usage Examples with Python
Commenting Folders with open source (Mixtral):
```
python .\comment_generator\main.py --source_folder  C:\Users\Sayalee\Projects\langchain\image_generator_bot --target_folder C:\Users\Sayalee\Projects\commented_projects\image_generator_bot --model_type mixtral
```
Commenting Folders with openai:
```
python .\comment_generator\main.py --source_folder  C:\Users\Sayalee\Projects\langchain\image_generator_bot --target_folder C:\Users\Sayalee\Projects\commented_projects\image_generator_bot --model_type chatgpt
```
Comment Single file with openai:
```
python .\comment_generator\main.py --source_folder C:\Users\Sayalee\Projects\langchain\summarykeywords\summarykeywords\extractkeyword.py --target_folder C:\Users\Sayalee\Projects\commented_projects\extract_keyword --model_type chatgpt
```
Comment Single file with open source (Mixtral):
```
python .\comment_generator\main.py --source_folder C:\Users\Sayalee\Projects\langchain\summarykeywords\summarykeywords\extractkeyword.py --target_folder C:\Users\Sayalee\Projects\commented_projects\extract_keyword --model_type mixtral
```

## Usage Examples with Executable
