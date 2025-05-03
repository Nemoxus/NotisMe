from dotenv import load_dotenv
import os
import requests

load_dotenv()

'''
hf_api_key = os.getenv("HUGGINGFACE_API_KEY")
print(hf_api_key)
'''


def classify_text(text, labels):
    hf_api_key = os.getenv("HUGGINGFACE_API_KEY")
    api_url = os.getenv("HUGGINGFACE_API_URL_text_classf")
    headers = {"Authorization": f"Bearer {hf_api_key}"}
    
    payload = {
        "inputs": text,
        "parameters": {"candidate_labels": labels}
    }
    
    response = requests.post(api_url, headers=headers, json=payload)
    return response.json()

# Example use:

inp = input("Enter a sentence:")
x = True
z = []
while(x):
    print("Enter Choice:\n1 to enter a tag\n2 to view the tags\n3 to close list")
    ch = int(input())

    if ch == 1:
        tag = input("Enter a tag:")
        z.append(tag)
    elif ch == 2:
        print(z)
    elif ch == 3:
        x = False
result = classify_text(inp,z)
print(result)
