import os
import requests
import re
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# You can switch to other models like:
# https://api-inference.huggingface.co/models/knkarthick/MEETING_SUMMARY
API_URL = os.getenv("HUGGINGFACE_API_URL_text_summr")
headers = {
    "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"
}

def summarize_note(note_text):
    payload = {"inputs": note_text}
    response = requests.post(API_URL, headers=headers, json=payload)

    print("📡 Status Code:", response.status_code)
    print("📨 Raw Response Text:", response.text)  # Debugging FTW

    try:
        result = response.json()

        if isinstance(result, dict) and 'error' in result:
            return [{"summary_text": f"⚠️ API Error: {result['error']}"}]

        return result
    except requests.exceptions.JSONDecodeError as e:
        print("⚠️ JSON decode failed:", e)
        return [{"summary_text": "❌ Unable to summarize due to API error or invalid response."}]

def clean_note_md(text):
    # Remove markdown headers
    text = re.sub(r'#+ ', '', text)
    # Remove code blocks
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    # Remove horizontal lines or excessive whitespace
    text = re.sub(r'\n{2,}', '\n', text)
    return text.strip()

if __name__ == "__main__":
    print("📋 Paste your note below. Hit Enter then Ctrl+D (or Ctrl+Z on Windows) when done:\n")
    try:
        user_input = ""
        while True:
            line = input()
            user_input += line + "\n"
    except EOFError:
        pass

    cleaned_note = clean_note_md(user_input)

    if len(cleaned_note.strip()) < 20:
        print("✋ Input too short or not meaningful enough to summarize.")
    else:
        summary = summarize_note(cleaned_note)
        print("\n📝 Summarized Note:\n", summary[0]['summary_text'])
