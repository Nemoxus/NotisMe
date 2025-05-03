import os
from dotenv import load_dotenv

load_dotenv()

# path to your Obsidian vault
VAULT_PATH = os.getenv("OBSIDIAN_VAULT_PATH")

def get_all_markdown_files(vault_path):
    notes = []
    for root, dirs, files in os.walk(vault_path):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                notes.append(full_path)
    return notes

def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

# Example usage:
files = get_all_markdown_files(VAULT_PATH)
for file in files:
    content = read_markdown_file(file)
    print(f"\n📝 {file}\n{content[:300]}...")  # just a preview
