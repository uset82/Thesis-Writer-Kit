# Thesis Writer Kit

<div align="center">

![Thesis Writer Kit](https://img.shields.io/badge/Thesis-Writer_Kit-blue?style=for-the-badge)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)

**AI-powered thesis research and writing assistant with verified citations**

> Generate authentic, research-backed academic drafts using specialized AI agents that verify every source against 200M+ academic papers.

</div>

---

## ⚡ 1-Click Easy Setup

### 🤖 For Any AI IDE (Antigravity, Cursor, Codex, Claude Code, Windsurf)
Just copy and paste this single prompt directly into your AI IDE chat:

```text
install this project git clone https://github.com/uset82/Thesis-Writer-Kit.git
```

> **What happens automatically:** Your AI assistant will clone the repository, load the 5 specialist agents, activate the 69-pattern de-AI humanizer and voice calibration skills, install all dependencies, and prepare the 200M+ paper research engine!

---

### 💻 1-Line Terminal Clone & Auto-Setup

**Windows (PowerShell):**
```powershell
git clone https://github.com/uset82/Thesis-Writer-Kit.git; cd Thesis-Writer-Kit; .\setup.ps1
```

**macOS / Linux (Bash):**
```bash
git clone https://github.com/uset82/Thesis-Writer-Kit.git && cd Thesis-Writer-Kit && chmod +x setup.sh && ./setup.sh
```

---

## 🚀 Quick Action Table

| Goal | Command / Action | What it does |
|---|---|---|
| 🔍 **Literature Search** | `python -m opendraft.cli "Topic" --expose` | Searches 200M+ papers and builds outline with citations |
| ✍️ **Draft Chapter** | `python -m opendraft.cli "Topic" --level master` | Generates full chapter draft with APA 7 verified citations |
| 🛡️ **Audit AI Signals (0–100)** | `python -m opendraft.cli audit --text "..."` | Deterministic 0–100 score & exact line-by-line pattern flags |
| 🎭 **Humanize & Match Voice** | `python -m opendraft.cli humanize --text "..." --sample sample.txt` | De-AIs prose using 69 empirical rules and matches your rhythm |
| 📄 **Export to LibreOffice / Word** | `python -m opendraft.cli export --text draft.md --format odt` | Converts to styled `.odt`, `.docx`, or `.pdf` with LaTeX Math |
| 🌐 **Interactive Web Interface** | `cd tools/yourwrite; npm start` | Launches web UI on `http://localhost:3000` |

---

## What's Included

| Component | Count | Description |
|-----------|-------|-------------|
| **Agents** | 5 | Specialist AI personas (research, writing, citations, editing, humanizing) |
| **Skills** | 7 | Domain knowledge modules (69 anti-AI patterns, voice calibration, APA citations, LibreOffice automation) |
| **Workflows** | 6 | Slash command procedures (/research, /draft, /cite, /humanize, /export, /status) |
| **Engine** | 1 | OpenDraft - Research draft generator, citation engine, and CLI auditor |
| **Tools** | 3 | YourWrite Web UI, Avoid-AI-Writing Detector Engine, and WriterAgent LibreOffice Suite |

---

## Structure

```
.agent/
├── agents/           # 5 Specialist Agents
├── skills/           # 7 Skills (including 69-category AI bypass & LibreOffice integration)
├── workflows/        # 6 Slash Commands
├── rules/            # Workspace Rules (including avoid-ai-writing.md)
├── opendraft/        # Research Engine (Python CLI + Humanizer + Detector + Export bridge)
└── ARCHITECTURE.md   # Full documentation
Papers/               # Stored PDFs, extracted text, and BibTeX literature
chatgpt_research/     # Transcripts, notes, and research archives
tools/
├── yourwrite/        # Standalone Web UI (TypeScript / Express / Gemini)
├── detector/         # Deterministic 0-100 Scoring & Preservation Engine (Node.js)
└── writeragent/      # LibreOffice Extension, Python Compute Service & MCP Server
```

---

## Agents

| Agent | Description |
|-------|-------------|
| `research-agent` | Deep literature search across 200M+ papers |
| `writing-agent` | Academic drafting with thesis structure |
| `citation-agent` | APA 7 citation verification and formatting |
| `editor-agent` | Grammar, coherence, and style refinement |
| `humanizer-agent` | 33-pattern AI cleanup and author voice calibration |

---

## Skills

| Skill | Purpose |
|-------|---------|
| `academic-writing` | Thesis structure, PEEL paragraphs, academic tone |
| `citation-management` | APA 7 formatting, DOI verification, bibliography |
| `thesis-structure` | Chapter organization, argument mapping |
| `ai-bypass` | 33-pattern anti-AI rules (YourWrite), voice calibration |
| `research-methods` | Literature review, source screening |
| `harper` | Grammar checking and language polish |

---

## Workflows

Invoke workflows with slash commands:

| Command | Description |
|---------|-------------|
| `/research` | Deep literature search on a topic |
| `/draft` | Generate section draft with citations |
| `/cite` | Verify and format citations |
| `/humanize` | Apply 33-pattern stealth writing & voice calibration (`--sample`) |
| `/export` | Export to PDF, Word, or LaTeX |
| `/status` | Check project and draft status |

### Example Usage

```
/research "AI governance in energy sector"
/draft introduction --words 600
/cite --style apa7 --verify
/humanize --section introduction
```

---

## Using with AI Assistants

### With Cursor/VS Code Copilot

The agents and skills are automatically available. Use workflows like:
- "Follow the research-agent to find papers on AI ethics"
- "Apply the humanizer skill to this paragraph"
- "Use /draft to write the methodology section"

### OpenDraft Engine (CLI)

```bash
# Quick research exposé (outline + sources)
python -m opendraft.cli "Impact of AI on Education" --expose

# Full thesis draft
python -m opendraft.cli "Sustainable Energy in Norway" --level master --lang en
```

---

## OpenDraft vs ChatGPT

| Feature | ChatGPT | Thesis Writer Kit |
|---------|---------|-------------------|
| Citation verification | ❌ Hallucinates | ✅ Verified against real DBs |
| Long-form writing | ❌ Hits limits | ✅ 20,000+ words |
| Academic structure | ❌ Generic | ✅ Thesis chapters |
| Source search | ❌ No | ✅ 200M+ papers |
| AI detection bypass | ❌ No | ✅ Stealth strategies |
| Export formats | ❌ Copy/paste | ✅ PDF, Word, LaTeX |

---

## Project Configuration

Current thesis configuration (editable in `.agent/config/thesis.yaml`):

| Field | Value |
|-------|-------|
| **Word Limit** | 4,000 words |
| **Citation Style** | APA 7 |
| **Degree Level** | Master |

---

## Documentation

- [Architecture Guide](.agent/ARCHITECTURE.md) - Full system documentation
- [OpenDraft README](.agent/opendraft/README.md) - Engine documentation
- [Quick Start Guide](RUN.md) - Getting started

---

## Requirements

- Python 3.10+
- Google Gemini API Key (free)

---

## License

MIT © 2026

---

<div align="center">

**Built for researchers who need authentic, verifiable academic writing.**

</div>
