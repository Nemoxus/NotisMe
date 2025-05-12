import os
import json
from datetime import datetime

def get_all_md_files(vault_path):
    """Recursively collects all .md files from the vault directory."""
    md_files = []
    for root, _, files in os.walk(vault_path):
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                md_files.append(full_path)
    return md_files

def get_file_metadata(file_path, vault_path):
    """Extracts metadata for a single markdown file."""
    stat = os.stat(file_path)
    created = datetime.fromtimestamp(stat.st_ctime).isoformat()
    modified = datetime.fromtimestamp(stat.st_mtime).isoformat()
    
    return {
        "reading_name": os.path.splitext(os.path.basename(file_path))[0],
        "relative_path": os.path.relpath(file_path, vault_path),
        "created": created,
        "modified": modified
    }

def index_vault(vault_path, output_path='vault_index.json'):
    """Indexes all markdown files and saves metadata as JSON."""
    all_md_files = get_all_md_files(vault_path)
    index = []

    for md_file in all_md_files:
        metadata = get_file_metadata(md_file, vault_path)
        index.append(metadata)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=4)
    
    print(f"✅ Indexed {len(index)} markdown files. Output written to: {output_path}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Index all markdown files in a vault.")
    parser.add_argument("vault_path", help="Path to your markdown vault folder")
    parser.add_argument("--output", default="vault_index.json", help="Output JSON file path")
    
    args = parser.parse_args()
    index_vault(args.vault_path, args.output)
