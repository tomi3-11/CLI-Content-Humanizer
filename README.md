# Humanizer AI CLI

A command-line tool that rewrites text to sound more **natural, human-like, and fluent** using the Gemini API.

---

## Features
- Handles up to **2000 words**.
- Multiple **tones** (formal, casual, storytelling, etc.).
- Works via **Gemini API**.
- Accepts **text file input** or **manual paste**.
- Optionally saves **output to file**.

---

## Project Structure
```text
humanizer-ai/
│
├── humanizer.py        # core logic (Gemini API integration)
├── cli.py              # command-line interface
├── requirements.txt    # dependencies
└── README.md           # usage guide

```

## Setup
1. Clone or create this folder
```bash
git clone https://github.com/tomi3-11/CLI-Content-Humanizer
cd CLI-Content-Humanizer
```
2. Install dependencies:
```bash
pip install -r requirements.txt

```

3. Set your Gemini API key:
```bash
export GEMINI_API_KEY="your_api_key_here" # For linux/mac
set GEMINI_API_KEY="your_api_key_here" # For windows

```
## Usage
Option 1: From a text File
```bash
python cli.py --input article.txt --tone conversational --output humanized.txt

```
Option 2: Paste text manually
```bash

python cli.py

# Then paste your content and press Enter twice to start processing.
```

## Example
Input:
```bash
The project was completed by the team successfully. It was finished before the deadline.

```
Output (tone: friendly):
```bash
Our team wrapped up the project ahead of schedule - a big win for everyone involved!

```
---
## License
MIT License © 2025
  

