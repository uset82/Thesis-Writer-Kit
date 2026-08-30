# LibreOffice & WriterAgent Integration Skill

> Agent skill for interacting with LibreOffice Writer, Calc, and Draw documents, generating native .odt/.docx/.pdf formats, converting LaTeX math into LibreOffice Math objects, and computing NumPy statistics on data tables.

---

## 🎯 Core Capabilities

1. **Document Export & Conversion:**
   - Convert OpenDraft Markdown research drafts directly into formatted OpenDocument (`.odt`), Microsoft Word (`.docx`), and `.pdf` files.
   - Preserves citation tags `{cite_XXX}` and structured headings.
2. **LaTeX Math → LibreOffice Math Equations:**
   - Translates LaTeX inline `$formula$` and display `$$formula$$` into native LibreOffice Math formulas.
3. **NumPy & Pandas Empirical Table Compute:**
   - Ingest data tables from `.csv` or markdown, compute descriptive statistics (mean, std dev, median, range, regressions), and embed formatted summary tables into thesis drafts.
4. **Model Context Protocol (MCP) Live Document Editing:**
   - Connects to LibreOffice WriterAgent MCP server (`http://localhost:18765/mcp`) to inspect open documents, apply redlines, insert comments, and adjust styles live in the GUI editor.

---

## 🛠️ Export Usage

### Command Line:
```powershell
cd .agent/opendraft/engine
python -m opendraft.cli export --text path/to/draft.md --format odt
python -m opendraft.cli export --text path/to/draft.md --format docx
python -m opendraft.cli export --text path/to/draft.md --format pdf
```

---

## 🔌 LibreOffice MCP Server Setup

To allow AI agents in Antigravity or Claude to inspect and edit open LibreOffice documents:
1. Open LibreOffice Writer with the **WriterAgent** extension installed (`tools/writeragent/`).
2. Start the MCP server from **WriterAgent → Settings → MCP Server** or run:
   ```powershell
   python tools/writeragent/compute_service/mcp_server.py
   ```
3. Connect your AI agent via MCP configuration using `http://localhost:18765/mcp` or stdio transport.
