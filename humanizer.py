import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# configure GEMINI API
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def humanize_text(text: str, tone: str = "natural") -> str:
    """
    Humanizes and rewrites the given text to sound more fluent and human-like.

    Args:
        text (str): Input text (up to ~2000 words)
        tone (str): Desired tone, e.g. 'formal', 'friendly', 'storytelling'

    Returns:
        str: Humanized version of the text
    """
    prompt = f"""
    Rewrite the following text to sound natural, human-like, and {tone} in tone.
    Preserve meaning, improve flow, and remove robotic phrasing.

    TEXT:
    {text}
    """
    
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip() if response.text else "[No output returned]"