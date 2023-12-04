import datetime
import pathlib
import uuid
import together

from comment_generator.configuration.config import cfg



def add_comments(model_name, code):
    together.api_key = cfg.together_api_key
    output = together.Complete.create(
                    prompt = f"""Can you please add comments to all functions using the reStructuredText Docstring Format for the following code: {code}""", 
                    model =  model_name, 
                    max_tokens = 500,
                    temperature = 0.1,
                    top_k = 50,
                    top_p = 0.6,
                    repetition_penalty = 1.1,
                    stop = ['<human>', '\n\n']
                    )
    output_model = output["output"]["choices"][0]["text"]
    d = datetime.datetime.now()
    date_now = d.date()
    code_comment = cfg.code_comment
    index = model_name.find('/') #stores the index of a substring or char
    model = model_name[index+1:]
    code_comment_path = pathlib.Path(f"{code_comment}/exec_{date_now}")
    if not code_comment_path.exists():
        code_comment_path.mkdir(exist_ok=True, parents=True)
    with open(code_comment_path/f"{model}.txt", mode="w") as f:
        f.write("============")
        f.write('\n')
        f.write(output_model)
        f.write('\n')
        f.write("============")
        f.write('\n')
    return output_model


if __name__ == "__main__":
    for model in cfg.updated_model_list:
        print(model)
        code = """
        ```def save_to_file(model, output, time_exec, question):
            code_output = pathlib.Path(f"/tmp/togetherai_output")
            if not code_output.exists():
                code_output.mkdir(exist_ok=True, parents=True)
            d = datetime.datetime.now()
            date_now = d.date()
            question_name = question.replace(" ", "")
            question_name = question_name.replace("\n", "")

            with open(code_output/f"{date_now}_{question_name}_together_report.md", mode="a+") as f:
                f.write("\n")
                f.write("=========")
                f.write("\n")
                f.write("# "+ model)
                f.write("\n")
                f.write("## "+ str(date_now))
                f.write("\n")
                f.write(question + "\n" +output)
                f.write("\n")
                f.write(str(time_exec) + "seconds")
                f.write("\n")
                f.write("=========")```
        """ 
        print(add_comments(model, code))
        
