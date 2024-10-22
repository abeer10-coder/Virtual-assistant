import google.generativeai as genai

gemini_api = 'Api-key'
genai.configure(api_key=gemini_api)
model = genai.GenerativeModel("gemini-1.5-flash")
Query = input('Enter your query:')
response = model.generate_content(Query)
print(response.text)