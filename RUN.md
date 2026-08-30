# How to Run: Thesis Research & Writing Expert

This project allows you to generate authentic, research-backed academic drafts using a purpose-built AI engine, 33-pattern anti-AI humanization, and author voice calibration.

---

## 1. Setup

### Prerequisites
- Python 3.10 or higher
- Node.js 18+ (for YourWrite Web UI)
- A Google Gemini API Key (Free)

### Installation
1. **Python Engine**:
   ```powershell
   cd .agent/opendraft/engine
   pip install -r requirements.txt
   ```

2. **YourWrite Web UI (Optional)**:
   ```powershell
   cd tools/yourwrite
   npm install
   ```

---

## 2. Running the Engine (OpenDraft CLI)

Navigate to `.agent/opendraft/engine`:
```powershell
cd .agent/opendraft/engine
```

### Key Commands:
* **Interactive Mode**:
  ```powershell
  python -m opendraft.cli
  ```
* **Quick Research Exposé** (Outline + Sources):
  ```powershell
  python -m opendraft.cli "Impact of AI on Education" --expose
  ```
* **Full Thesis Draft**:
  ```powershell
  python -m opendraft.cli "Sustainable Energy in Norway" --level master --lang en
  ```
* **Audit Text & Score AI Tells (0-100)**:
  ```powershell
  python -m opendraft.cli audit --text "Text to audit..."
  ```
* **Humanize & De-AI Draft** (69-Pattern Multi-Tier Engine):
  ```powershell
  python -m opendraft.cli humanize --text "Additionally, this transformative landscape stands as a testament..."
  ```
* **Export to ODT / Word / PDF** (LibreOffice & Math Bridge):
  ```powershell
  python -m opendraft.cli export --text path/to/draft.md --format odt
  python -m opendraft.cli export --text path/to/draft.md --format docx
  python -m opendraft.cli export --text path/to/draft.md --format pdf
  ```

---

## 3. Running YourWrite Web Interface

To launch the browser-based humanizer UI:
```powershell
cd tools/yourwrite
cp .env.example .env   # Add your GOOGLE_API_KEY
npm start
```
Then open `http://localhost:3000` in your browser.

---

## 4. Working with the Agent in Chat

1. **Research Literature**: Type `/research "My Topic"`
2. **Draft Section**: Type `/draft introduction --words 600`
3. **Verify Citations**: Type `/cite --verify`
4. **Humanize & Match Voice**: Type `/humanize introduction --sample "path/to/sample.md"`
5. **Export**: Type `/export --format pdf,docx`
