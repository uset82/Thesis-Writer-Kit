# How to Run: Thesis Research & Writing Expert

This project allows you to generate authentic, research-backed academic drafts using a purpose-built AI engine.

## 1. Setup

### Prerequisites
- Python 3.10 or higher
- A Google Gemini API Key (Free)

### Installation
Open a terminal in `.agent/opendraft` and install dependencies:

```powershell
cd .agent/opendraft
pip install -r requirements.txt
```

## 2. Running the Engine (OpenDraft)

The research engine is located in `.agent/opendraft`. To run the interactive generator:

1.  Navigate to the engine directory:
    ```powershell
    cd .agent/opendraft/engine
    ```

2.  Run the CLI:
    ```powershell
    python -m opendraft.cli
    ```

3.  **First Run**: Select `setup` (or run `python -m opendraft.cli setup`) to enter your Google API Key.

### Quick Commands (from `.agent/opendraft/engine`)

*   **Interactive Mode**:
    ```powershell
    python -m opendraft.cli
    ```
*   **Quick Research Exposé** (Outline + Sources):
    ```powershell
    python -m opendraft.cli "Impact of AI on Education" --expose
    ```
*   **Full Thesis Draft**:
    ```powershell
    python -m opendraft.cli "Sustainable Energy in Norway" --level master --lang en
    ```

### Advanced: Direct Engine Usage
You can also run the pipeline directly (bypassing the CLI wrapper):
```powershell
cd .agent/opendraft/engine
python draft_generator.py --topic "Your topic" --level master
```

## 3. Working with the Agent (Manual Mode)

If you are working directly with the AI Assistant (me) to write your thesis interactively:

1.  **Start a Section**: Tell me "I want to start the Introduction."
2.  **I will follow**: `.agent/writing_workflow.md`.
3.  **I will apply**: `.agent/thesis_writing_strategy.md` (Stealth Mode).
4.  **I will allow you**: To verify sources and inject your own analysis.

---
**Note**: The engine (`opendraft`) generates the *base draft*. The Agent (me) helps you *refine, expand, and humanize* it using the strategy files.
