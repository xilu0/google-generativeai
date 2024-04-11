import google.generativeai as genai
import os

genai.configure(api_key=os.environ['API_KEY'])

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("What is the meaning of life?")

print(response.text)