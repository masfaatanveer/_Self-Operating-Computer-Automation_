<h1 align="center">🧠 Self Operating Computer Automation</h1>
<h3 align="center">By Masfa Tanveer</h3>

<p align="center">
  <strong>A multimodal agent framework to automate your computer like a human.</strong><br/>
  Watch the screen, decide intelligently, and act via mouse + keyboard to complete tasks autonomously.
</p>

<div align="center">
  <img src="https://github.com/OthersideAI/self-operating-computer/blob/main/readme/self-operating-computer.png" width="760" alt="Demo Screenshot"/>
</div>

---

## 🚀 Overview

This project turns your computer into a **self-operating intelligent agent** that can:

- See the screen using screenshots (like a human)
- Understand it using **GPT‑4o**, **Gemini**, **Claude 3**, or **LLaVa**
- Act with mouse and keyboard to achieve objectives (click buttons, type text, navigate apps)
- Optionally use **voice commands** and **OCR detection** for better precision

---

## 📽 Demo Video

> 👇 Terminal-based usage of the `operate` command with AI automation:

https://github.com/OthersideAI/self-operating-computer/assets/42594239/9e8abc96-c76a-46fb-9b13-03678b3c67e0

---

## ✨ Key Features

- 🧠 Multimodal AI Models Supported: `GPT‑4o`, `Claude 3`, `Gemini Pro Vision`, `LLaVa`
- 🎯 Operates with real mouse & keyboard like a human
- 🧩 Modular skill system with plugin support
- 🎤 Voice objective input (`--voice` flag)
- 🔍 OCR vision mode for clickable element mapping
- 🖥️ Local model support via [Ollama](https://ollama.ai)

---

## ⚙️ Install and Run

### 1. Install via pip

```bash
pip install self-operating-computer-automation
```

### 2. Run the agent

```bash
operate
```

### 3. Enter your API key

You’ll be prompted to enter an OpenAI, Claude, or Gemini key  
→ [Get OpenAI Key](https://platform.openai.com/account/api-keys)

---

## 🛑 Required Permissions

This app needs **screen recording** and **accessibility control** on Windows/Mac.

<div align="center">
  <img src="https://github.com/OthersideAI/self-operating-computer/blob/main/readme/terminal-access-1.png" width="300" />
  <img src="https://github.com/OthersideAI/self-operating-computer/blob/main/readme/terminal-access-2.png" width="300" />
</div>

---

## 🧠 Supported Modes

| Mode Flag | Description |
|-----------|-------------|
| *(default)* | `-m gpt-4-with-ocr` for best click accuracy |
| `-m gemini-pro-vision` | Use Gemini Pro Vision |
| `-m claude-3` | Use Claude 3 |
| `-m llava` | Use local model via Ollama |
| `--voice` | Voice input support for hands-free operation |

---

## 🔥 Using LLaVa Locally via Ollama

```bash
# Step 1: Install Ollama (https://ollama.ai/download)

# Step 2: Pull model
ollama pull llava

# Step 3: Start Ollama
ollama serve

# Step 4: Run your agent
operate -m llava
```

---

## 🧩 Voice Mode (Optional)

```bash
# Clone the repo and install audio dependencies
git clone https://github.com/masfaatanveer/_Self-Operating-Computer-Automation_.git
cd self-operating-computer-automation
pip install -r requirements-audio.txt

# Install system audio libs
# Mac:
brew install portaudio

# Linux:
sudo apt install portaudio19-dev python3-pyaudio

# Run with voice
operate --voice
```

---

## 🛠 Development Setup

```bash
git clone https://github.com/masfaatanveer/_Self-Operating-Computer-Automation_.git
cd _Self-Operating-Computer-Automation_
pip install -r requirements.txt
```

Run the dev build:
```bash
operate
```

---

## 📂 Repo Structure

```
📁 self-operating-computer-automation/
├── operate                     # CLI entry
├── core/                       # Main agent logic
├── vision/                     # Screenshot and OCR tools
├── plugins/                   # Custom skill scripts
├── models/                    # API model wrappers
├── requirements.txt
├── requirements-audio.txt
└── README.md
```

---

## 📌 Tags / Topics

```
automation
self-operating
windows-automation
multimodal-ai
gpt-4o
gemini-pro-vision
claude-3
ollama
agentic-ai
ai-agent
python
autopilot
```

---

## 👨‍💻 Created by Masfa Dhillon

[GitHub](https://github.com/masfaatanveer) • [LinkedIn](https://linkedin.com/in/masfa-tanveer-500474235)

---

## 📄 License

MIT License — free for personal and commercial use. Attribution appreciated!

---
