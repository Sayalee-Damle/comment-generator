import os
from pathlib import Path
import click
from comment_generator.configuration.log_factory import logger
import comment_generator.backend.comment_files as comment
from comment_generator.config_toml import cfg



click.echo("===============================")
click.echo(f"Welcome to the Comment Generator Tool!", color = False)
click.echo("===============================")
click.echo(f"Get your code commented within a few minutes with ease", color = True)
click.echo("Pre-requisites: Have a togetherAI key for using opensource models or the openAI key for using chatGPT in the .env file", color = True)
click.echo("Follow the steps from the --help if you need more details (python .\comment_generator\main.py --help)", color = True)
click.echo("Please provide the details- ", color = True)

@click.command()
@click.option(
    "--source_folder",
    type=click.Path(exists=True),
    prompt="Source folder Path (please remove any \"s that the path may have)",
    help="Source folder with the files which are going to be commented.",
)
@click.option(
    "--target_folder",
    prompt="Target folder Path (please remove any \"s that the path may have)",
    help="Target folder into which the commented code will be copied.",
)
@click.option(
    "--model_type",
    type=click.Choice(["openai", "togetherai"]),
    default="togetherai",
    prompt="Model type",
    required=True,
)



    
 
def comment_generator(source_folder: str, target_folder: str, model_type: str):
    """Comment Generator.

    Small Python utility with which you can comment your code using either an Open Source model or ChatGPT.
    Please note that you will need to have either an OpenAI key from https://platform.openai.com/ or
    a TogetherAI key from https://www.together.ai/

    You need to set the API key in the environment variable before using this utility.

    \b
    This tool requires a set of environment variables that are typically read from an .env file.
    
    \b
    For more information about needed variables please check the .env_local file in our repository: 
    https://github.com/Sayalee-Damle/comment-generator

    \b
    If you want to change the togetherAI opensource model, go to ./backend/together_ai_streaming.py and change the model.
    
    """
    
    logger.info("source_folder: %s", source_folder)
    logger.info("target_folder: %s", target_folder)
    target_folder_path = Path(target_folder)
    if not target_folder_path.exists():
        target_folder_path.mkdir(parents=True)
        logger.info("target folder created: %s", target_folder)
    logger.info("model_type: %s", model_type)
    
    match model_type:
        case "togetherai":
            if cfg.together_api_key != None:
                
                comment.comment_python_files_opensource(source_folder, target_folder)
            else:
                click.echo("Please add the OpenAI API key in your .env file and restart the code")
                exit()
                
        case "openai":
            if cfg.openai_api_key == None:
                click.echo("Please add the OpenAI API key in your .env file and restart the code")
                exit()
            else:
                comment.comment_python_files_gpt(source_folder, target_folder)
    click.echo("===============================")
    click.echo(f"Please check your commented code in the target folder: {target_folder}")
    click.echo("===============================")

 


if __name__ == "__main__":
    comment_generator()
