import os 
import openai
openai.api_key = "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" # api키
prompt='한국의수도가 어디야?' #입력 프롬프트
completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role":"user","content":prompt}
        ]
    )
print(completion)
