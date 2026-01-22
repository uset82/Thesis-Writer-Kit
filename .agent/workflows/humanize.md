# /humanize - AI Detection Bypass Workflow

> Apply stealth writing strategies using the humanizer-agent.

---

## Command Usage

```
/humanize
/humanize section-name
/humanize introduction --aggressive
/humanize --check-only
```

---

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--section NAME` | Specific section to humanize | all |
| `--aggressive` | Maximum transformation | false |
| `--check-only` | Analyze without changing | false |
| `--preserve-citations` | Keep citation formatting | true |

---

## Workflow Steps

### Step 1: AI Marker Detection
```
SCAN for:
□ Generic statements (no specifics)
□ Consistent sentence length
□ Repetitive transitions
□ "In conclusion" / "It is important"
□ Perfect balance ("On one hand...")
□ Bullet point lists
□ Flat, consistent tone
```

### Step 2: Report (if --check-only)
```
## AI Detection Analysis

**Document:** [filename]
**Risk Level:** [Low/Medium/High]

### Issues Found:
1. Line 23: Generic statement - "AI improves efficiency"
2. Line 45: AI marker phrase - "It is crucial to note"
3. Lines 50-70: Consistent sentence length (avg: 18 words)
4. Line 89: "In conclusion" opener

### Recommendations:
- Add 5 specific details (names, numbers)
- Vary sentence length
- Remove 3 AI marker phrases
```

### Step 3: Transform Text
```
AGENT: humanizer-agent
SKILL: ai-bypass

For each issue:
1. Inject specificity
2. Vary syntax
3. Add voice elements
4. Remove AI markers
```

### Step 4: Quality Check
```
After transformation:
□ No AI markers remain
□ Specifics added to each paragraph
□ Sentence length varies (<10 and >30)
□ Rhetorical questions added
□ Transitions varied
□ Read-aloud test passes
```

---

## Example Invocation

```
User: /humanize introduction

Agent Response:

## Humanization Report: Introduction

### Before Analysis
- **AI Risk Level:** Medium
- **Issues:** 4 generic statements, 2 AI markers, low burstiness

### Transformations Applied

#### 1. Specificity Injection
**Before:** "AI technologies are transforming the energy sector."
**After:** "Equinor's $330 million investment in AI—spread across 700 offshore installations since 2020—exemplifies how digital transformation reshapes North Sea operations."

#### 2. Sentence Burstiness
**Before:** Average sentence length: 18 words (range: 15-22)
**After:** Average: 19 words (range: 4-38)

#### 3. AI Marker Removal
- Removed: "It is important to note that..."
- Removed: "In conclusion..."
- Replaced: "crucial" → showed with evidence

#### 4. Voice Addition
- Added rhetorical question: "Why does this matter?"
- Added direct address: "Consider the case of..."

### After Analysis
- **AI Risk Level:** Low
- **Specifics per paragraph:** 2.5 (target: 2+)
- **Sentence variation:** ✓ Passes burstiness check

---

**Word count change:** 598 → 612 (+2%)
**Ready for submission:** Yes
```

---

## Transformation Rules

### Specificity Rules

| Generic | Specific |
|---------|----------|
| "the company" | "Equinor" |
| "significant savings" | "$330 million in savings" |
| "recently" | "since 2020" |
| "many workers" | "1,200 maintenance technicians" |

### Sentence Variation Rules

| Type | Target |
|------|--------|
| Short (<10 words) | 15-20% of sentences |
| Medium (10-25 words) | 50-60% of sentences |
| Long (>25 words) | 20-30% of sentences |

### Voice Injection Rules

| Element | Frequency |
|---------|-----------|
| Rhetorical question | 1 per major section |
| Direct address | 1-2 per page |
| Authorial stance | Every analysis paragraph |

---

## Aggressive Mode

When `--aggressive` is used:

1. **Double specificity** - Every sentence gets a specific
2. **Maximum burstiness** - Include 2-3 word sentences
3. **Colloquialisms** - Add informal phrasing
4. **Object-first** - Use unusual syntax
5. **Number variation** - "a fifth" instead of "20%"

---

## Integration

| Receives From | Purpose |
|---------------|---------|
| `/draft` | Raw drafts |
| `/cite` | Verified text |

| Sends To | Purpose |
|----------|---------|
| `/export` | Final output |
| Human review | Final check |

---

## Quality Checklist

- [ ] No "In conclusion" or "It is important"
- [ ] Every paragraph has specific (name/number/date)
- [ ] Sentence length varies significantly
- [ ] No more than 2 consecutive same transitions
- [ ] At least 1 rhetorical question
- [ ] Reads naturally aloud
- [ ] Citations preserved correctly
