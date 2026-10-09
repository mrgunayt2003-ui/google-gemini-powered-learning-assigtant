import google.generativeai as genai

class EduGenieAIService:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def generate_learning_response(self, prompt: str, emotion: str = "neutral") -> str:
        system_instruction = f"You are an empathetic learning assistant. User emotion is {emotion}."
        response = self.model.generate_content(f"{system_instruction}\nUser: {prompt}")
        return response.text