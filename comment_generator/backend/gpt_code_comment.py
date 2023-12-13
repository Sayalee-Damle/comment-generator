from openai import OpenAI

from comment_generator.config_toml import cfg


client = OpenAI()
open_ai_key = cfg.openai_api_key




def get_human_message(code):

    return f"""Given  input is:
    
    {code}
    
    Please add comments to the code in reStructuredText Docstring Format.
    use markdown
    
    """
def code_commentor(code):
    open_ai_key = cfg.openai_api_key
    response = client.chat.completions.create(
    model=cfg.model_gpt,
    response_format={"type": "json_object" },
    messages=[
        {"role": "system", "content": "You are an expert in understanding the given code and putting comments for it."},
        {"role": "human", "content": get_human_message(code)}
    ]
    )
    return response.choices[0].message.content

if __name__ == '__main__':
    code = """
        def save_text_to_file(text):
            logger.info("in 2nd func")
            try:
                
                with open(cfg.transcribed_text / f"{uuid.uuid4()}.txt", "w") as file:
                    file.write(text)
                    logger.info("successful")
                    return "success"
            except Exception as e:
                logger.exception("error")
                return str(e)
        """
    code_commentor(code)