# Academic Papers & Literature Repository

> Storage directory for thesis source literature, downloaded PDFs, extracted text summaries, and BibTeX citations.

---

## Directory Organization

```
Papers/
├── pdfs/               # Raw downloaded academic PDF papers
├── extracted/          # Plaintext (.txt or .md) extracted text for AI context
├── bibtex/             # Reference .bib files for citation management
└── notes/              # Literature review summaries and reading notes
```

---

## File Naming Conventions

To ensure the research agent and citation compiler can parse and cite sources seamlessly:
- **PDFs:** `Author_Year_KeyTerm.pdf` (e.g., `Smith_2023_TransformerEfficiency.pdf`)
- **Extracted Text:** `Author_Year_KeyTerm.txt`
- **BibTeX:** `references.bib` or `Author_Year.bib`

---

## How Agents Use This Folder

- **`research-agent`**: Searches and reads papers stored in this folder when generating outlines.
- **`citation-agent`**: Verifies claims against text excerpts and compiles APA 7 citations.
- **OpenDraft Engine**: Automatically indexes and caches cited paper metadata in `.citation_cache_orchestrator.json`.
