# /draft - Section Drafting Workflow

> Generate thesis section drafts using the writing-agent.

---

## Command Usage

```
/draft "section name"
/draft introduction --words 600
/draft "theoretical framework" --sources sources.md
/draft methodology --outline-first
```

---

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--words N` | Target word count | from structure |
| `--sources FILE` | Source file to use | sources.md |
| `--outline-first` | Generate outline before draft | false |
| `--peel` | Enforce PEEL paragraphs | true |
| `--humanize` | Apply AI bypass strategies | true |

---

## Workflow Steps

### Step 1: Load Context
```
READ: 
- Research question and thesis statement
- Sources/bibliography
- Section requirements (word count, purpose)
- Previous sections (for continuity)
```

### Step 2: Create Outline (if --outline-first)
```
OUTPUT:
## Section: [Name]

**Main Claim:** [One sentence]

**Paragraph Plan:**
1. Opening - [topic] - [source]
2. Body 1 - [topic] - [source]
3. Body 2 - [topic] - [source]
4. Closing - [topic] - [link to next section]

Proceed with draft? [Y/n]
```

### Step 3: Data Injection
```
Before writing, compile:
- Names: [list]
- Numbers: [list]
- Dates: [list]
- Key citations: [list]
```

### Step 4: Draft Section
```
AGENT: writing-agent
SKILLS: academic-writing, thesis-structure

APPLY:
- PEEL paragraph structure
- Integrated citations
- Sentence burstiness
- Specific details (names, numbers)
```

### Step 5: Insert User Prompts
```
Mark areas needing user input:

[INSERT YOUR ANALYSIS: How does this evidence relate to your argument?]

[INSERT DATA: Add your empirical findings here]

[VERIFY: Confirm this interpretation aligns with your thesis]
```

### Step 6: Quality Check
```
VERIFY:
- [ ] Word count within ±10% of target
- [ ] All claims have citations
- [ ] Topic sentences clear
- [ ] Transitions present
- [ ] No AI markers
```

---

## Example Invocation

```
User: /draft introduction --words 600 --outline-first

Agent Response:

## Section Outline: Introduction

**Main Claim:** AI governance at Equinor requires balancing efficiency with ethical workforce transition.

**Paragraph Plan:**
1. Hook - Equinor's $330M savings, the hidden cost (Equinor, 2023)
2. Context - Energy sector digital transformation trends
3. Problem - Governance gaps in AI deployment
4. Research Question + Thesis
5. Roadmap - Paper structure preview

Proceed with draft? [Y/n]

---

User: Y

Agent Response:

## Introduction [Draft - 612 words]

When Equinor announced $330 million in "digital value creation" in their 2023 annual report, the figure represented more than technological success—it marked a fundamental shift in how Norway's largest energy company would operate...

[...draft continues...]

[INSERT YOUR ANALYSIS: Add your perspective on why this research question matters for your specific context]

**Word count:** 612 (target: 600)
**Citations:** 5
**Status:** Ready for review

---

Next steps:
- `/humanize introduction` - Apply stealth strategies
- `/cite --verify` - Verify all citations
- Continue to `/draft "theoretical framework"`
```

---

## Section Templates

| Section | Structure |
|---------|-----------|
| Introduction | Hook → Context → Problem → RQ → Thesis → Roadmap |
| Theory/Lit Review | Overview → Concepts → Debates → Gaps → Contribution |
| Case Study | Background → Examples → Analysis → Limitations |
| Analysis | Findings → Interpretation → Comparison → Implications |
| Recommendations | Proposals → Implementation → Stakeholders → Future |
| Conclusion | Synthesis → Contribution → Implications → Final Thought |

---

## Integration

| Receives From | Purpose |
|---------------|---------|
| `/research` | Sources to cite |

| Sends To | Purpose |
|----------|---------|
| `/cite` | Verify citations |
| `/humanize` | Apply stealth strategies |
| `/export` | Format for output |
