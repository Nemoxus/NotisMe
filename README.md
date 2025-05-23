# 🧠 NotisMe — Terminal-Powered Second Brain

**NotisMe** is my no-nonsense, Obsidian-compatible, terminal-based second brain 🧠 built entirely from Markdown files and Python scripts. It's where thoughts are tracked, ideas are refined, and chaos gets version controlled — all without ever opening a browser tab.

---

## 📦 TL;DR

- 🧾 Markdown-based notes, organized into folders
- 💻 100% terminal-driven — no GUI, no plugins, no distractions
- 🐍 Python-powered scripts to automate my thought garden
- 🧠 Inspired by Zettelkasten, digital minimalism, and a hint of controlled chaos

---

## 📁 Project Structure

```bash
notisme/
├── notes/               # All Markdown notes — your vault
│   ├── daily/           # Daily logs and journal entries
│   ├── ideas/           # Permanent notes (evergreen)
│   ├── projects/        # Project documentation & concepts
│   ├── books/           # Book and paper summaries
│   └── templates/       # Note templates (for structure)
├── scripts/             # Python tools for automation
│   ├── indexer.py       # Parses and links notes
│   ├── note_creator.py  # CLI for creating new notes
│   └── search.py        # Fast grep-style terminal search
├── .gitignore
├── requirements.txt     # Python dependencies
├── README.md
└── venv/                # Virtual environment (ignored)
⚙️ Features
No plugins. No frontend. Just you, your thoughts, and your terminal.

📌 Create new notes from terminal with auto-formatting

🔗 Parse and link notes using filename IDs and tags

🔍 Grep-like fuzzy search through note content & titles

🧼 Auto-organize or clean note metadata

📂 Maintain a consistent folder structure

✅ Easily git-track changes and roll back when needed

🚀 Quickstart
bash
Copy
Edit
git clone https://github.com/raj/notisme.git
cd notisme
Set up your Python environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
Run your scripts:

bash
Copy
Edit
python scripts/note_creator.py    # Create a new note
python scripts/search.py          # Search notes
python scripts/indexer.py         # Generate interlink index
Open and edit notes in your favorite terminal text editor like vim, nano, or neovim.

🧠 Why NotisMe?
Because the best interface is no interface.
Because sometimes clicking around slows you down.
Because version-controlling your thoughts is peak 21st-century enlightenment.
Because Markdown is immortal.

📌 Future Plans
>
    Add backlinks tracking in terminal

    Tag-based filtering system

    CLI dashboard to summarize notes

    Cron-based auto-indexing

    Natural language summary generator (AI-powered maybe?)


🧊 Git Hygiene
>
    venv/ is ignored. Keep your scripts clean.

    Version control everything with Git — no excuses.

    Use meaningful commits. You're committing thoughts, not just code.

⚖️ License
MIT — Use, fork, build your own second brain, and if it becomes sentient, I take no responsibility 👾

🤝 Built by
Raj
aka The guy who put his brain in a folder named notes/ and never looked back.
GitHub: [your GitHub profile link here]

---

“In an age of forgetting, this is my memory stick. And I built it in a terminal.”