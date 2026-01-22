# /research - Literature Search Workflow

> Deep literature search on a topic using the research-agent.

---

## Command Usage

```
/research "topic or research question"
/research "AI governance in energy sector" --sources 10
/research "sustainability ethics" --recent --annotate
```

---

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--sources N` | Number of sources to find | 10 |
| `--recent` | Limit to last 5 years | false |
| `--annotate` | Create annotated bibliography | false |
| `--databases` | Specify databases (comma-separated) | all |

---

## Workflow Steps

### Step 1: Parse Request
```
INPUT: User's topic or research question
OUTPUT: Search strategy with keywords
```

### Step 2: Database Search
```
AGENT: research-agent
ACTION: Search across academic databases
- OpenAlex (primary)
- Semantic Scholar
- CrossRef
- arXiv (if technical)
- PubMed (if health-related)
```

### Step 3: Screen Results
```
For each result:
1. Read title and abstract
2. Apply CRAAP criteria
3. Categorize: Include / Maybe / Exclude
```

### Step 4: Create Output
```
OUTPUT FORMAT:
## Research Results: [Topic]

### Included Sources (N)
1. **Author (Year)** - Title
   - DOI: https://doi.org/xxx
   - Relevance: [brief note]

### Maybe Sources (N)
[Same format, for manual review]

### Search Strategy
- Databases: [list]
- Query: [query used]
- Date range: [if filtered]
```

### Step 5: Annotate (if --annotate)
```
For each included source:
- Full APA 7 citation
- 5-7 line annotation
- Relevance tags
```

---

## Example Invocation

```
User: /research "AI ethics frameworks" --sources 5 --recent --annotate

Agent Response:
## Research Results: AI Ethics Frameworks

Searched: OpenAlex, Semantic Scholar
Date filter: 2021-2025
Results found: 234
Screened: 50
Included: 5

### Included Sources

#### 1. Floridi & Cowls (2019)
**Citation:** Floridi, L., & Cowls, J. (2019). A unified framework...
**DOI:** https://doi.org/10.1162/99608f92.8cd550d1
**Annotation:** Synthesizes existing AI ethics frameworks into five principles...
**Tags:** #framework #principles #foundational

[...continues for all 5 sources]
```

---

## Integration

| Handoff To | When |
|------------|------|
| `/draft` | Sources ready for writing |
| `/cite` | Sources need verification |

---

## Success Criteria

- [ ] Sources verified (DOIs work)
- [ ] Relevance confirmed
- [ ] Mix of source types (empirical, theoretical)
- [ ] Annotations complete (if requested)
- [ ] Search strategy documented
