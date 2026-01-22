# /export - Export Workflow

> Export thesis to PDF, Word, or LaTeX format.

---

## Command Usage

```
/export
/export --format pdf
/export --format docx --template academic
/export --format latex --bibliography
```

---

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--format` | Output format (pdf, docx, latex, md) | pdf |
| `--template` | Template to use | academic |
| `--bibliography` | Include reference list | true |
| `--toc` | Include table of contents | true |
| `--output FILE` | Output filename | thesis_[date] |

---

## Workflow Steps

### Step 1: Gather Content
```
COLLECT:
- All section drafts
- Bibliography/references
- Title page info
- Abstract (if present)
```

### Step 2: Compile Document
```
ORDER:
1. Title page
2. Abstract (if present)
3. Table of Contents (if --toc)
4. Main sections (in order)
5. References
6. Appendices (if present)
```

### Step 3: Apply Formatting
```
TEMPLATE: academic
- Font: Times New Roman, 12pt
- Spacing: Double
- Margins: 1 inch
- Page numbers: Bottom center
- Headings: APA style
```

### Step 4: Generate Output
```
Using Pandoc or OpenDraft engine:
- Markdown → PDF (via LaTeX)
- Markdown → DOCX
- Markdown → LaTeX source
```

### Step 5: Quality Check
```
VERIFY:
□ All sections included
□ Page numbers continuous
□ Citations formatted correctly
□ References complete
□ Formatting consistent
```

---

## Example Invocation

```
User: /export --format pdf --bibliography

Agent Response:

## Export Report

### Document Summary
- **Title:** Governing AI and Sustainability at Equinor
- **Sections:** 6
- **Word Count:** 4,012
- **Citations:** 24
- **References:** 18

### Compilation
✓ Title page generated
✓ Abstract included
✓ Table of contents created
✓ Sections compiled (6/6)
✓ References formatted (APA 7)
✓ Page numbers added

### Output
📄 **File:** thesis_2026-01-22.pdf
📁 **Location:** ./output/
📊 **Pages:** 18

### Preview
[First page preview would appear here]

---

**Export complete.** 
File saved to: `./output/thesis_2026-01-22.pdf`
```

---

## Format Options

### PDF
- Best for: Final submission
- Engine: Pandoc + LaTeX
- Template: academic (APA style)

### DOCX (Word)
- Best for: Advisor review, track changes
- Engine: Pandoc
- Template: Standard academic

### LaTeX
- Best for: Technical theses, custom formatting
- Engine: Direct export
- Includes: .tex source files

### Markdown
- Best for: Version control, portability
- Engine: None (raw export)
- Includes: All source files

---

## Template Options

| Template | Use For |
|----------|---------|
| `academic` | Standard APA thesis |
| `minimal` | Simple formatting |
| `formal` | Institutional submission |
| `draft` | Review copy (line numbers) |

---

## OpenDraft Engine Export

For full thesis generation with OpenDraft:

```bash
cd .agent/opendraft/engine
python -m opendraft.cli "topic" --level master --export pdf
```

### OpenDraft Export Options
- `--export pdf` - PDF output
- `--export docx` - Word output
- `--export latex` - LaTeX source
- `--export all` - All formats

---

## Manual Export (Pandoc)

If OpenDraft not available:

```bash
# PDF
pandoc thesis.md -o thesis.pdf --pdf-engine=xelatex

# Word
pandoc thesis.md -o thesis.docx --reference-doc=template.docx

# LaTeX
pandoc thesis.md -o thesis.tex
```

---

## Pre-Export Checklist

Run these before exporting:

```
/cite --verify     # Verify all citations
/humanize --check  # Check for AI markers
```

---

## Integration

| Receives From | Purpose |
|---------------|---------|
| `/humanize` | Final polished text |
| `/cite` | Verified citations |

| Output | Destination |
|--------|-------------|
| PDF/DOCX/LaTeX | Submission ready |
