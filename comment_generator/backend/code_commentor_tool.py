
import datetime
import pathlib
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain

from comment_generator.configuration.toml_support import read_prompts_toml
from comment_generator.configuration.config import cfg

prompts = read_prompts_toml()


def prompt_factory():
    prompt = prompts['comments']
    system_message_prompt = SystemMessagePromptTemplate.from_template(
        template=prompt['system_message']
    )
    human_message_prompt = HumanMessagePromptTemplate.from_template(
        template=prompt['human_message']
    )
    messages = [system_message_prompt, human_message_prompt]
    chat_prompt = ChatPromptTemplate.from_messages(messages)
    return chat_prompt

def document_tool(code):
    prompt = prompt_factory()
    chain = LLMChain(llm=cfg.llm, prompt=prompt, verbose=cfg.verbose_llm)
    return chain.run({"code": code})

def code_commentor(code):

    output = document_tool(code)
    d = datetime.datetime.now()
    d = str(d).replace(":", "")
    d = d.replace(" ","")
    date_now = d[:14]
    print(date_now)
    code_comment = cfg.code_comment
    code_comment_path = pathlib.Path(f"{code_comment}/exec_{date_now}")
    if not code_comment_path.exists():
        code_comment_path.mkdir(exist_ok=True, parents=True)
    with open(code_comment_path/f"commented_code.py", mode="w") as f:
        f.write("============")
        f.write('\n')
        f.write(output)
        f.write('\n')
        f.write("============")
        f.write('\n')
    return output

if __name__ == "__main__":
    for model in cfg.updated_model_list:
        print(model)
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
        print(code_commentor(code))