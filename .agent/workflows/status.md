# /status - Project Status Workflow

> Display thesis project and agent status.

---

## Command Usage

```
/status
/status --sections
/status --citations
/status --full
```

---

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--sections` | Show section progress | true |
| `--citations` | Show citation status | false |
| `--full` | Complete status report | false |
| `--wordcount` | Show word counts | true |

---

## Workflow Steps

### Step 1: Gather Project Info
```
READ:
- Thesis configuration
- Section files
- Sources/bibliography
- Draft status
```

### Step 2: Calculate Progress
```
For each section:
- Word count / target
- Draft status (not started, in progress, complete)
- Citation count
```

### Step 3: Generate Report
```
Display formatted status board
```

---

## Example Output

```
User: /status

Agent Response:

═══════════════════════════════════════════════════════════
                    THESIS STATUS BOARD
═══════════════════════════════════════════════════════════

📚 PROJECT: Governing AI and Sustainability at Equinor
🎓 LEVEL: Master's Thesis
📝 TARGET: 4,000 words
📅 DATE: 2026-01-22

───────────────────────────────────────────────────────────
                      SECTION PROGRESS
───────────────────────────────────────────────────────────

Section              Status        Words    Target   Progress
─────────────────────────────────────────────────────────────
1. Introduction      ✅ Complete    612      600     ████████████ 102%
2. Theory Framework  🔄 Draft       520      600     ████████░░░░  87%
3. Case Study        📝 Outline     150      800     ██░░░░░░░░░░  19%
4. Ethical Analysis  ⏳ Not Started   0     1000     ░░░░░░░░░░░░   0%
5. Recommendations   ⏳ Not Started   0      800     ░░░░░░░░░░░░   0%
6. Conclusion        ⏳ Not Started   0      400     ░░░░░░░░░░░░   0%
─────────────────────────────────────────────────────────────
TOTAL                              1,282    4,200              32%

───────────────────────────────────────────────────────────
                      CITATION STATUS
───────────────────────────────────────────────────────────

📖 Total Sources: 18
✅ Verified: 15
⚠️ Pending: 2  
❌ Failed: 1

───────────────────────────────────────────────────────────
                      QUALITY CHECKS
───────────────────────────────────────────────────────────

Check                           Status
──────────────────────────────────────
APA 7 Formatting               ⚠️ 2 issues
AI Detection Risk              ✅ Low
Patchwriting Check             ✅ Passed
Citation Coverage              ⚠️ 85%

───────────────────────────────────────────────────────────
                      NEXT ACTIONS
───────────────────────────────────────────────────────────

1. 📝 Complete: Theoretical Framework (need 80 more words)
2. ✏️ Draft: Case Study section
3. 🔍 Fix: 2 citation formatting issues
4. 📚 Verify: 1 unverified source

───────────────────────────────────────────────────────────

💡 Suggested command: /draft "case study" --words 800
```

---

## Full Status Report

```
User: /status --full

[Includes all of above plus:]

───────────────────────────────────────────────────────────
                      SOURCE DETAILS
───────────────────────────────────────────────────────────

Source                          Type        Used In
──────────────────────────────────────────────────────────
Floridi (2019)                 Journal      Intro, Theory
Equinor (2023)                 Report       Intro, Case
ILO (2015)                     Policy       Theory, Recs
Zuboff (2019)                  Book         Theory
[...]

───────────────────────────────────────────────────────────
                      TIMELINE
───────────────────────────────────────────────────────────

Date        Action                    Sections
──────────────────────────────────────────────────────────
2026-01-20  Created                   -
2026-01-21  Drafted                   Introduction
2026-01-22  In Progress               Theory Framework

───────────────────────────────────────────────────────────
                      FILES
───────────────────────────────────────────────────────────

File                            Status      Words
──────────────────────────────────────────────────────────
drafts/introduction.md          Complete    612
drafts/theory.md                Draft       520
drafts/case-study.md            Outline     150
sources.md                      Active      18 entries
```

---

## Status Indicators

| Icon | Meaning |
|------|---------|
| ⏳ | Not Started |
| 📝 | Outline Only |
| 🔄 | Draft In Progress |
| ✅ | Complete |
| ⚠️ | Needs Attention |
| ❌ | Problem |

---

## Integration

| Works With | Purpose |
|------------|---------|
| All workflows | Track progress |
| Project files | Read status |

---

## Quick Actions from Status

Based on status, suggested commands:

| Status | Suggested Command |
|--------|-------------------|
| Section not started | `/draft "section"` |
| Citation issues | `/cite --verify` |
| AI risk high | `/humanize --check` |
| Ready to submit | `/export --format pdf` |
