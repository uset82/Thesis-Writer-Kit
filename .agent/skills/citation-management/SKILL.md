# Citation Management Skill

> APA 7 formatting, DOI verification, bibliography management.

---

## 🎯 Skill Purpose

Ensure every citation is verifiable, properly formatted, and correctly integrated.

---

## APA 7 Quick Reference

### Journal Article

```
Author, A. B., & Author, C. D. (Year). Title of article. *Journal Name*, Volume(Issue), pages. https://doi.org/xxxxx
```

**Example:**
> Floridi, L., & Cowls, J. (2019). A unified framework of five principles for AI in society. *Harvard Data Science Review*, 1(1), 1-15. https://doi.org/10.1162/99608f92.8cd550d1

### Book

```
Author, A. B. (Year). *Title of book* (Edition ed.). Publisher.
```

**Example:**
> Zuboff, S. (2019). *The age of surveillance capitalism: The fight for a human future at the new frontier of power*. PublicAffairs.

### Edited Book Chapter

```
Author, A. B. (Year). Title of chapter. In E. E. Editor (Ed.), *Title of book* (pp. xx-xx). Publisher.
```

### Website (with author)

```
Author, A. B. (Year, Month Day). Title of page. Site Name. https://url
```

### Website (no author)

```
Title of page. (Year, Month Day). Site Name. https://url
```

### Corporate Author

```
Organization Name. (Year). *Title of document*. https://url
```

**Example:**
> Equinor ASA. (2023). *2023 sustainability report*. https://www.equinor.com/sustainability

---

## In-Text Citations

### Basic Patterns

| Authors | First Citation | Subsequent |
|---------|---------------|------------|
| 1 | (Smith, 2023) | (Smith, 2023) |
| 2 | (Smith & Jones, 2023) | (Smith & Jones, 2023) |
| 3+ | (Smith et al., 2023) | (Smith et al., 2023) |

### Special Cases

| Situation | Format |
|-----------|--------|
| Direct quote | (Smith, 2023, p. 45) |
| Paraphrase | (Smith, 2023) |
| Multiple sources | (Jones, 2022; Smith, 2023) |
| Same author, same year | (Smith, 2023a, 2023b) |
| No date | (Smith, n.d.) |
| Secondary source | (Original, as cited in Smith, 2023) |

### Narrative vs. Parenthetical

**Parenthetical:**
> The framework identifies five key principles (Floridi, 2019).

**Narrative:**
> Floridi (2019) identifies five key principles in the framework.

---

## Citation Integration

### Level 1: Basic (Avoid)
> Studies show AI improves efficiency (Smith, 2023; Jones, 2022; Brown, 2021).

### Level 2: Integrated (Better)
> Smith (2023) demonstrates that AI improves efficiency, a finding consistent with earlier work by Jones (2022).

### Level 3: Analytical (Best)
> While Smith's (2023) quantitative analysis shows a 15% efficiency gain, Jones (2022) qualifies this by noting that such gains often come at the cost of workforce reduction—a tension that Brown (2021) terms the "automation paradox."

---

## Verification Checklist

### For Each Citation

- [ ] Author name spelled correctly
- [ ] Year matches source
- [ ] In-text matches reference list entry
- [ ] DOI/URL works
- [ ] Page numbers for direct quotes

### For Reference List

- [ ] Alphabetical order by first author
- [ ] Hanging indent (0.5 inch)
- [ ] Double-spaced
- [ ] No bullet points or numbers
- [ ] All sources cited in text included
- [ ] No sources not cited in text

---

## Common Errors

| Error | Correct |
|-------|---------|
| (Smith, et al., 2023) | (Smith et al., 2023) — no comma |
| Smith et. al. | Smith et al. — no period after "et" |
| (Smith 2023) | (Smith, 2023) — comma needed |
| According to Smith (2023, p. 5) | Correct for quotes only |
| *Title of article* | Title of article — no italics for articles |

---

## DOI Formatting

### Standard Format
```
https://doi.org/10.1000/xxxxx
```

### Old Format (Update These)
```
doi: 10.1000/xxxxx → https://doi.org/10.1000/xxxxx
```

### Verification
Test DOIs at: https://doi.org

---

## Reference List Template

```markdown
## References

Author, A. B. (Year). Title of work. *Journal*, Volume(Issue), pages. https://doi.org/xxxxx

Author, C. D., & Author, E. F. (Year). *Title of book*. Publisher.

Organization Name. (Year). *Title of report*. https://url
```

---

## Source Quality Indicators

| Indicator | Preferred |
|-----------|-----------|
| Publication date | <5 years for empirical |
| Peer reviewed | Yes |
| Impact factor | Higher is generally better |
| Citation count | Consider for seminal works |
| DOI present | Required when available |

---

## Avoiding Plagiarism

### Patchwriting Warning Signs

| Risk | Fix |
|------|-----|
| Same sentence structure | Completely restructure |
| Only 1-2 words changed | Paraphrase fully |
| Unusual phrases retained | Use your own language |

### Safe Paraphrasing Process

1. Read the original
2. Close the source
3. Write in your own words
4. Check against original
5. Add citation

---

## Integration with Agents

| Agent | How This Skill Helps |
|-------|---------------------|
| `research-agent` | Format new sources |
| `writing-agent` | Integrate citations |
| `citation-agent` | Primary skill |
| `editor-agent` | Verify formatting |
