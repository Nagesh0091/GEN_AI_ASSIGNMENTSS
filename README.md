# 🤖 GEN_AI_ASS: Generative AI Assignments

A collection of my Generative AI assignments, from Python basics and NLP fundamentals to Gemini, LangChain, prompt engineering and a live Streamlit app.

---

## 🌐 Live Apps (Public URLs)

| App | Description | Live URL |
|-----|-------------|----------|
| 💌 **AI Greeting Card Assistant** (`app.py`) | Basic version: enter occasion, recipient and tone to get a greeting message | 👉 `PASTE-YOUR-PUBLIC-URL-HERE` |
| 💌 **AI Greeting Card Assistant, Advanced** (`app_advanced.py`) | Dropdowns with an "Other" option, 3 samples (1 handwritten prompt + 2 AI-written prompts), language and length options, styled UI, download | 👉 `PASTE-YOUR-PUBLIC-URL-HERE` |

---

## 📁 Repository Structure

```
GEN_AI_ASS-master/
├── 01-intro-to-python/
│   └── intro_to_python.ipynb
├── 02-nlp-fundamentals-1/
│   └── tokenization_embeddings_.ipynb
├── 03-nlp-fundamentals-2/
│   └── sentiment_analysis.ipynb
├── 04-nlp-fundamentals-3/
│   └── nlp_fundamentals_3.ipynb
├── 05-advanced-nlp-generative-models/
│   └── gemini_tasks.ipynb
├── 06-chatgpt-in-action/
│   ├── AI_Prompting_Showcase.md
│   └── prompting_showcase.ipynb
├── 07-generative-ai/
│   ├── Assignment7_Gemini_Output.md
│   └── generative_ai.ipynb
├── 08-langchain-basics/
│   └── study_buddy.ipynb
├── 09-intro-llms-prompt-engineering/
│   ├── Assignment9_Output.md
│   └── gadgetron_chatbot.ipynb
├── 10ai_greeting_app/
│   ├── app.py
│   ├── app_advanced.py
│   └── requirements.txt
├── .gitignore
└── README.md
```

---

## 📚 Assignment Overview

| # | Folder | What it covers |
|---|--------|----------------|
| 01 | `01-intro-to-python` | Python fundamentals and basics needed for AI work |
| 02 | `02-nlp-fundamentals-1` | Tokenization and embeddings |
| 03 | `03-nlp-fundamentals-2` | Sentiment analysis |
| 04 | `04-nlp-fundamentals-3` | More NLP fundamentals |
| 05 | `05-advanced-nlp-generative-models` | Tasks using Google Gemini (generative models) |
| 06 | `06-chatgpt-in-action` | Prompting showcase with different prompting techniques (notebook + written output) |
| 07 | `07-generative-ai` | Generative AI with Gemini (notebook + output file) |
| 08 | `08-langchain-basics` | LangChain basics: a "Study Buddy" application |
| 09 | `09-intro-llms-prompt-engineering` | Intro to LLMs and prompt engineering: the "Gadgetron" chatbot |
| 10 | `10ai_greeting_app` | Streamlit web app that writes greeting card messages with Gemini |

---

## 💌 Project 10: AI Greeting Card Assistant

### `app.py` (basic)
- Text inputs for occasion and recipient, a dropdown for tone (Funny, Formal, Heartfelt)
- A prompt built from the user's inputs (prompt engineering with an f-string)
- Sends the prompt to Gemini and displays the message

### `app_advanced.py` (advanced)
- **30 occasions, 23 recipients and 10 tones** in dropdowns, each with **✏️ Other (type your own)**
- **3 samples** per click:
  - Sample 1: prompt written by me
  - Samples 2 and 3: the **AI writes the prompt first**, then that prompt generates the message
- Extra options: message length, language (English, Hindi, Marathi, Hinglish and more), sender name, personal details
- Styled UI: gradient header, tabs, message cards, balloons, copy box and download button

### Access
Open the apps only through the public links in the **Live Apps** table at the top of this page. No installation or setup is needed.

---

## 🛠️ Tech Stack
Python · Jupyter Notebooks · NLP · Google Gemini · LangChain · Streamlit

## 🔐 Security Note
API keys are never uploaded. `.env` and `secrets.toml` files are excluded with `.gitignore`.

---

## 🚀 Git Commands: Step by Step (How This Repo Was Uploaded)

### Step 1: Check / install tools (one time)
```bash
git --version
winget install --id GitHub.cli
gh --version
```
Close and reopen the terminal after installing. On Mac: `brew install gh`.

### Step 2: Log in to GitHub (one time)
```bash
gh auth login
gh auth status
```
Choose GitHub.com → HTTPS → Yes → Login with a web browser, then paste the one-time code in the browser.

### Step 3: Tell git who you are (one time)
```bash
git config --global user.name "Your Name"
git config --global user.email "your-github-email@example.com"
```

### Step 4: Go to the main folder
```bash
cd path\to\GEN_AI_ASS-master
```

### Step 5: Make sure `.gitignore` is in the main folder with these lines
```
.env
.env.*
!.env.example
secrets.toml
**/.streamlit/secrets.toml
venv/
.venv/
env/
__pycache__/
*.py[cod]
.ipynb_checkpoints/
.vscode/
.idea/
.DS_Store
Thumbs.db
```

### Step 6: Initialize git
```bash
git init
```

### Step 7: Check the secret files are ignored
```bash
git check-ignore -v 06-chatgpt-in-action/.env 07-generative-ai/.env 08-langchain-basics/.env 09-intro-llms-prompt-engineering/.env 10ai_greeting_app/.streamlit/secrets.toml
```
Every file must print with a `.gitignore` rule. If one prints nothing, fix `.gitignore`.

### Step 8: Add all files and check
```bash
git add .
git status
```
The list must **not** contain any `.env` or `secrets.toml`. Extra check, which must print nothing:
```bash
# Windows
git ls-files | findstr /i "\.env secrets.toml"
# Mac / Linux
git ls-files | grep -E "\.env|secrets.toml"
```
If a secret file was added by mistake:
```bash
git rm -r --cached .
git add .
```

### Step 9: Scan notebooks for API keys
```bash
git grep --cached -n -I -E "AIza|sk-[A-Za-z0-9]{20,}|api_key *= *[\"'][A-Za-z0-9]"
```
- Prints nothing → safe, continue.
- Prints a line → replace the key with `os.getenv("GEMINI_API_KEY")`, use **Clear All Outputs** in that notebook, save, run `git add .` and repeat this step.

### Step 10: Commit
```bash
git commit -m "Add GenAI assignments 01-10 including greeting card app"
git branch -M main
```

### Step 11: Create the repo on GitHub and push (one command)
```bash
gh repo create GEN_AI_ASS --public --source=. --remote=origin --push
```
Use `--private` instead of `--public` for a private repo.

**Alternative without `gh`:** create an empty repo on github.com (leave README, .gitignore and license **unticked**), then:
```bash
git remote add origin https://github.com/YOUR-USERNAME/GEN_AI_ASS.git
git push -u origin main
```
If it asks for a password, use a Personal Access Token (GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic) → tick `repo`).

### Step 12: Verify on GitHub
```bash
gh repo view --web
```
Open every folder and make sure there is no `.env` and no `secrets.toml`. Search the repo for `AIza`, which should find nothing.

### Later changes (every time you edit or add files)
```bash
git add .
git status
git commit -m "Describe what you changed"
git push
```

### If a key was ever uploaded
Deleting the file is not enough, because it stays in git history. Delete the key in Google AI Studio, create a new one, and keep it only in your local `.env` / `secrets.toml`.

---

⭐ If you like this project, give the repo a star!
