from pathlib import Path
import click
from comment_generator.configuration.log_factory import logger
import comment_generator.backend.comment_files as comment

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
    This tool requires a set on environemnt variable that are typically read from an .env file.
    
    \b
    For more information about needed variables please check the .env_local file in our repository: 
    https://github.com/Sayalee-Damle/comment-generator
    
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
            comment.comment_python_files_opensource(source_folder, target_folder)

        case "openai":
            comment.comment_python_files_gpt(source_folder, target_folder)
    click.echo("===============================")
    click.echo(f"Please check your commented code in the target folder: {target_folder}")

 


if __name__ == "__main__":
    comment_generator()