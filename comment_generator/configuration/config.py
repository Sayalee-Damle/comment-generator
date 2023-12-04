from langchain.llms import Together
from pathlib import Path
from dotenv import load_dotenv
import os


from comment_generator.configuration.log_factory import logger


load_dotenv()

class Config:

    model_list = [
        "togethercomputer/alpaca-7b",
        "Austism/chronos-hermes-13b",
        "togethercomputer/CodeLlama-7b-Python",
        "togethercomputer/CodeLlama-7b",
        "togethercomputer/CodeLlama-13b-Python",
        "togethercomputer/CodeLlama-34b-Python",
        "togethercomputer/llama-2-7b-chat",
        "togethercomputer/llama-2-13b-chat",
        "togethercomputer/llama-2-70b-chat",
        "mistralai/Mistral-7B-v0.1",
        "Gryphe/MythoMax-L2-13b",
        "NousResearch/Nous-Hermes-Llama2-13b",
        "NousResearch/Nous-Hermes-Llama2-70b",
        "NousResearch/Nous-Hermes-llama-2-7b",
        "teknium/OpenHermes-2p5-Mistral-7B",
        "togethercomputer/Qwen-7B-Chat",
        "Undi95/ReMM-SLERP-L2-13B",
        "lmsys/vicuna-13b-v1.5-16k",
        "lmsys/vicuna-13b-v1.5",
        "lmsys/vicuna-7b-v1.5",
        "WizardLM/WizardCoder-15B-V1.0",
        "WizardLM/WizardLM-70B-V1.0"
    ]

    updated_model_list = [
        "togethercomputer/alpaca-7b",
        "Austism/chronos-hermes-13b",
        "togethercomputer/CodeLlama-34b-Python",
        "togethercomputer/llama-2-7b-chat",
        "togethercomputer/llama-2-13b-chat",
        "togethercomputer/llama-2-70b-chat",
        "teknium/OpenHermes-2p5-Mistral-7B",
        "Undi95/ReMM-SLERP-L2-13B",
        "lmsys/vicuna-13b-v1.5-16k",
        "lmsys/vicuna-13b-v1.5",
        "lmsys/vicuna-7b-v1.5",
        "WizardLM/WizardCoder-15B-V1.0",
        "WizardLM/WizardLM-70B-V1.0"
    ]

    def select_model(self, model_name_val, temperature_val, max_tokens_val, top_k_val):
            
        llm = Together(
            model = model_name_val,
            temperature= temperature_val,
            max_tokens= max_tokens_val,
            top_k= top_k_val,
            together_api_key= os.getenv("TOGETHER_API_KEY"),
            top_p = 0.7,
            repetition_penalty = 1
        )
        return llm


    project_root = Path(os.getenv("PROJECT_ROOT"))
    assert project_root.exists()

    together_api_key= os.getenv("TOGETHER_API_KEY")
    ui_timeout = int(os.getenv("UI_TIMEOUT"))

    code_output = Path(f"/tmp/togetherai_pylint")
    if not code_output.exists():
        code_output.mkdir(exist_ok=True, parents=True)

    code_comment = Path(f"/tmp/togetherai_code_comment")
    if not code_comment.exists():
        code_comment.mkdir(exist_ok=True, parents=True)

        
cfg = Config()

if __name__ == "__main__":
    print(cfg.project_root)