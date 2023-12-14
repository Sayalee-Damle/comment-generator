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
async def code_commentor(code):
    stream=False
    output = ""
    response = await cfg.open_ai_client.chat.completions.create(
        model=cfg.model_gpt,
        messages=[
            {"role": "system", "content": "You are an expert in understanding the given code and putting comments for it."},
            {"role": "user", "content": get_human_message(code)}
        ],
        stream=stream
        )
    if stream:
        output += str(response)
        return output
    choices = response.choices
    if len(choices) > 0:
        return choices[0].message.content
    else:
        return None
    

if __name__ == '__main__':
    import asyncio
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
    print(asyncio.run(code_commentor(code)))