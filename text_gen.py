import requests, os
from dotenv import load_dotenv

load_dotenv()
hf_api_key = os.getenv("HUGGINGFACE_API_KEY")

def generate_text(prompt):
    api_url = os.getenv("HUGGINGFACE_API_URL_text_gen")
    headers = {"Authorization": f"Bearer {hf_api_key}"}
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 300,
            "temperature": 0.7,
            "top_p": 0.9,
            "do_sample": True
        }
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()
        output = response.json()
        if isinstance(output, list) and 'generated_text' in output[0]:
            return output[0]['generated_text'].strip()
        elif isinstance(output, dict) and 'generated_text' in output:
            return output['generated_text'].strip()
        else:
            return "⚠️ Unexpected response format."
    except requests.exceptions.HTTPError as http_err:
        return f"❌ HTTP error: {http_err}"
    except Exception as e:
        return f"❌ Other error: {str(e)}"

def build_prompt(instruction, note):
    instruction = instruction.lower().strip()
    templates = {
        "quiz": f"Create a quiz based on this note:\n\n{note}",
        "title": f"Suggest 3 catchy titles for the following note:\n\n{note}",
        "blog": f"Write a short blog post based on this:\n\n{note}",
        "summary": f"Summarize the following note clearly:\n\n{note}",
        "recipe": f"Write a complete recipe based on:\n\n{note}",
        "tweet": f"Write a tweet summarizing this note in a witty way:\n\n{note}",
        "idea": f"Expand this short note into a creative ideation paragraph:\n\n{note}"
    }
    return templates.get(instruction, f"{instruction}\n\n{note}")

# 🌱 Second Brain Text Generator
print("🧠 Second Brain: AI Text Generator (Mixtral 8x7B Instruct)")
instruction = input("What do you want? (e.g., quiz, title, blog, recipe, summary, idea, tweet):\n> ")
note = input("Paste your note content:\n> ")

prompt = build_prompt(instruction, note)
output = generate_text(prompt)

print("\n✨ Generated Output:\n", output)
