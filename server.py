import base64
import os
from google.generativeai import types
from google.generativeai import GenerativeModel
import google.generativeai as genai
from dotenv import load_dotenv
from pydantic import BaseModel
import json

load_dotenv()


class suggestion(BaseModel):
    botname: str 
    botmsg: str

api_key= os.getenv('GEMINI_API_KEY')
genai.configure(api_key='AIzaSyDZtc-ET_3CcbBiiUSNFPgglVkTHb7K-Pc')


generation_config={
    'temperature':0.80,
    'response_mime_type': "text/plain",
    'response_mime_type': "application/json",
    'response_schema': suggestion,
}

model= genai.GenerativeModel(
    model_name="gemini-2.5-flash-preview-05-20",
    generation_config=generation_config
    )






def generate_prompt(username, usermessage):

    prompt =f"""
You are an AI game bot in a multiplayer chat room. You do not reply to every message.

Instead, you wait until 1 or 2 user messages have occurred, then interrupt with a surprise event or trivia game.

Your response must ONLY be in JSON format and should include:
- A random human-sounding name.
- A fun event like a trivia question, a “Would You Rather”, or a quick vote prompt.

Always return strictly valid JSON. Do not include explanations or comments.

Example format:
{{
  "botname": "Taylor Morris",
  "botmsg": "What planet is known as the Red Planet?"
}}

username: {username}  
usermessage: {usermessage}

Instructions:
- Generate random questions or games based on user message
- Only return valid JSON. Do not include any explanations or extra text.


"""


    
    try:
        input= model.generate_content([

            f'query: {prompt}',
            'output: ',
        ]   
        )
        input= json.loads(input.text) 

        botname= input['botname']
        
        botmsg= input['botmessage']

        print(f'botname test is {botname}')
        print(f'botmesg test is {botmsg}')

        return botname, botmsg 


    except Exception as e:
        print(f'error is : {e}')

    
    
 



if __name__ == "__main__":
    while True:
        prompt= input('YOU: ')
        if prompt.lower() in ['bye','exit', 'close', 'quit']:
            print('Goodbye')
            break
        botname, botmsg = generate_prompt(prompt)

        print(f'botname is {botname}')
        print(f'botmsg is {botmsg}')
