# /cite - Citation Verification Workflow

> Verify and format citations using the citation-agent.

---

## Command Usage

```
/cite --verify
/cite --format
/cite --check section.md
/cite --bibliography
```

---

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--verify` | Verify DOIs and sources exist | true |
| `--format` | Format to APA 7 | true |
| `--check FILE` | Check specific file | current draft |
| `--bibliography` | Generate reference list | false |
| `--fix` | Auto-fix formatting issues | false |

---

## Workflow Steps

### Step 1: Extract Citations
```
SCAN document for:
- Parenthetical: (Author, Year)
- Narrative: Author (Year)
- Reference list entries
```

### Step 2: Cross-Reference
```
For each in-text citation:
1. Find matching reference entry
2. Flag mismatches
3. Flag missing entries
```

### Step 3: Verify Sources (if --verify)
```
For each reference:
1. Check DOI resolves (CrossRef)
2. Verify author/year/title match
3. Flag unverifiable sources
```

### Step 4: Format Check (if --format)
```
Check APA 7 compliance:
- Italicization
- Punctuation
- Author format
- DOI format
```

### Step 5: Generate Report
```
## Citation Verification Report

**Document:** [filename]
**Date:** [date]
**Total Citations:** N

### ✅ Verified (N)
- (Author, Year) - DOI verified ✓

### ⚠️ Needs Review (N)
- (Author, Year) - [issue]

### ❌ Failed (N)
- (Author, Year) - Not found

### Formatting Issues (N)
- [description of issue]
```

---

## Example Invocation

```
User: /cite --verify --format

Agent Response:

## Citation Verification Report

**Document:** introduction.md
**Date:** 2026-01-22
**Total Citations:** 8

### ✅ Verified (6)
- (Floridi, 2019) - DOI: 10.1162/99608f92.8cd550d1 ✓
- (Equinor, 2023) - Corporate report verified ✓
- (ILO, 2015) - UN document verified ✓
- (Zuboff, 2019) - ISBN verified ✓
- (Smith et al., 2022) - DOI: 10.1000/xxx ✓
- (EU Commission, 2024) - Government source ✓

### ⚠️ Needs Review (1)
- (Brown, 2021) - DOI not found, manual check required
  - Suggested action: Verify publisher website

### ❌ Failed (1)
- (Wilson, 2024) - No matching record in any database
  - Suggested action: Remove or replace source

### Formatting Issues (2)
1. Line 45: "(Smith, et al., 2023)" → "(Smith et al., 2023)"
   - Remove comma before "et al."
   
2. Line 78: Missing DOI for Jones (2022)
   - Add: https://doi.org/10.xxx

---

**Summary:**
- 75% verified
- 2 issues to fix
- 1 source to replace

Run `/cite --fix` to auto-correct formatting issues.
```

---

## Bibliography Generation

```
User: /cite --bibliography

Agent Response:

## References

Equinor ASA. (2023). *2023 annual report and sustainability report*. https://www.equinor.com/reports

Floridi, L., & Cowls, J. (2019). A unified framework of five principles for AI in society. *Harvard Data Science Review*, 1(1). https://doi.org/10.1162/99608f92.8cd550d1

International Labour Organization. (2015). *Guidelines for a just transition towards environmentally sustainable economies and societies for all*. https://www.ilo.org/publications

Smith, J., Jones, A., & Brown, K. (2022). AI governance in the energy sector. *Journal of Energy Policy*, 45(3), 234-251. https://doi.org/10.1000/xxx

Zuboff, S. (2019). *The age of surveillance capitalism: The fight for a human future at the new frontier of power*. PublicAffairs.
```

---

## APA 7 Quick Fixes

| Issue | Fix |
|-------|-----|
| (Smith, et al.) | (Smith et al.) |
| doi: 10.xxx | https://doi.org/10.xxx |
| *Article Title* | Article title (no italics) |
| Missing period | Add period after each element |
| & in text | "and" in narrative, "&" in parenthetical |

---

## Integration

| Receives From | Purpose |
|---------------|---------|
| `/draft` | Drafts to verify |
| `/research` | New sources |

| Sends To | Purpose |
|----------|---------|
| `/humanize` | Clean text for final pass |
| `/export` | Bibliography for export |
