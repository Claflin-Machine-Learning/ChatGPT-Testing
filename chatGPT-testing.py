# "OpenAI's GPT-3/ChatGPT: Suggests, but not Corrects"
# Built-in Functions: https://www.programiz.com/python-programming/methods
import os
import time
from datetime import datetime
import openai
import json

os.chdir("./")
sleep_interval_sec = 2
open_ai_key = "OPENAI_API_KEY"

# Initialize the API key for OpenAI
if open_ai_key in os.environ:
    openai.api_key = os.environ[open_ai_key]
else: 
    raise ValueError(f"{open_ai_key} is not set in the environment.")

language_map = {
        "python":".py",
        "java": ".java",
        "c++":".cpp",
        "c": ".c",
        "kotlin":".kt",
        "css": ".css",
        "javascript":".js",
        "go": ".go"
}

def get_file_extension(language):
    return language_map.get(language.lower(), "Unknown")

def get_chatgpt_response(question):

    return openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role":"user", "content":question}]
    )

def process_chat_completions(completion):
    input_dict = completion.to_dict()
    output_dict = {}

    output_dict["id"] = completion.id
    output_dict["output"] = completion.choices[0].message.content

    return output_dict

def read_language_files_in_folder():

    current_folder = os.getcwd()

    source_folder = os.path.join(current_folder,"questions")

    languages = [f for f in os.listdir(source_folder) if os.path.isdir(os.path.join(source_folder, f))]

    for language in languages:

        questions_folder = os.path.join(source_folder,language)

        responses_folder = os.path.join(current_folder,"responses",language)

        response_folder_exists = os.path.exists(responses_folder)

        if not response_folder_exists:
            os.makedirs(responses_folder)

        language_files = [f for f in os.listdir(questions_folder) if f.endswith(get_file_extension(language))]
        
        response_file = f'response-{datetime.now().isoformat()}.txt'
    
        with open(responses_folder + "/" + response_file,"a") as append_file:
            
            for language_file in language_files:
                
                print(f'Processing... {language_file}')
                        
                with open(questions_folder + "/" + language_file, "r") as file:
                    
                    code = file.read()

                    question = f'Fix following {language} code:\n```\n{code}\n```'
                    
                    chat_completions = get_chatgpt_response(question)

                    output_dict = process_chat_completions(chat_completions)
                    content = f'\nchat_completion_id:\t{output_dict["id"]}\n\nquestion:\n\n{question}\n\nresponse:\n\n{output_dict["output"]}\n=======\n'

                append_file.write(content)
                append_file.flush()
                print(f"Done processing... {language_file}")
                time.sleep(sleep_interval_sec)

    print("Finished")

if __name__ == '__main__':
    read_language_files_in_folder()