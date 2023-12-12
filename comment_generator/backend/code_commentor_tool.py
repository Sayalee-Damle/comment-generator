import datetime
import pathlib
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain

from comment_generator.configuration.toml_support import read_prompts_toml
from comment_generator.config_toml import cfg

prompts = read_prompts_toml()


def prompt_factory():
    prompt = prompts["comments"]
    system_message_prompt = SystemMessagePromptTemplate.from_template(
        template=prompt["system_message"]
    )
    human_message_prompt = HumanMessagePromptTemplate.from_template(
        template=prompt["human_message"]
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
