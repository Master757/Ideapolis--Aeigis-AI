import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyBAsiuqIvsd3x5NA-FAM8yBqwchTHQlWBg"  
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash-latest')

def ask(question):
    try:
        answer = model.generate_content(question)
        text = answer.text.strip()

        if "{" in text and "}" in text:
            start = text.find("{")
            end = text.rfind("}") + 1
            text = text[start:end]
        return text
    except Exception as e:
        return "An error has occured"
