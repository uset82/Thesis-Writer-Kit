# AI Bypass & Avoid-AI-Writing Skill (Unified 69-Category Edition)

> Comprehensive AI-writing audit, preservation validation, and rewriting skill combining 69 empirical pattern categories, a 112-word 3-tier replacement dictionary, 5 preset voice profiles, and author writing sample calibration.

---

## 🎯 Modes of Operation

1. **Rewrite Mode (Default):**
   - Scans text for AI patterns.
   - Performs Pass 1 rewrite with voice calibration and academic specificity.
   - Performs Pass 2 self-audit to eliminate any surviving tells or em-dashes.
   - Runs preservation check to guarantee citations (`{cite_XXX}`), LaTeX math (`$...$`), and tables are intact.
2. **Detect Mode (`--check-only`):**
   - Runs deterministic pattern analysis.
   - Returns a 0-100 score (`Minimal`, `Some`, `Strong`, `Heavy`), document classification (`HUMAN_ONLY`, `MIXED`, `AI_ONLY`), and a categorized list of line-by-line flags without altering prose.
3. **Edit Mode (Targeted Surgical Edit):**
   - In-place minimal edits targeting only flagged sentences while leaving verified human sections completely untouched.

---

## 🎙️ Voice Profiles & Calibration

### Preset Profiles:
- **`technical`**: Crisp, precise, active voice, domain-accurate jargon, zero fluff.
- **`academic/professional`**: Rigorous epistemic hedging, reasoned stance, evidence-grounded arguments.
- **`casual`**: Conversational cadence, contractions, direct observations.
- **`warm`**: Empathetic, engaging, accessible explanation of complex findings.
- **`blunt`**: Direct, punchy, concise, no ceremony.

### Author Sample Matching:
When provided with an author's writing sample (`--sample <path>`):
- Match observed sentence length distributions (burstiness).
- Match transition style (abrupt vs. connector-driven).
- Match author's preferred vocabulary density.

---

## 📚 112-Entry 3-Tier Replacement Dictionary

### Tier 1A: High-Frequency AI Tells (Always Eliminate)
| Flagged AI Word / Phrase | Preferred Human Replacement |
|---|---|
| `delve` / `delve into` | examine, analyze, explore, look at |
| `tapestry` (abstract) | complexity, system, combination, mix |
| `testament to` / `stands as a testament` | shows, confirms, demonstrates |
| `vibrant` (figurative) | active, growing, dense |
| `landscape` (abstract noun) | field, market, domain, context |
| `pivotal` | key, important, central |
| `underscore` / `underscores` | highlights, indicates, shows |
| `interplay` | interaction, relationship, dynamic |
| `nestled in` | located in, based in |
| `watershed moment` | turning point, significant shift |
| `foster` / `fostering` | encourage, develop, build |
| `garner` / `garnered` | receive, collect, attract |

### Tier 1B: Wordiness & Clarity Edits
| Wordy AI Phrase | Concise Human Alternative |
|---|---|
| `in order to` | to |
| `due to the fact that` | because |
| `at this point in time` | currently, now |
| `has the ability to` | can |
| `serves as` / `stands as` | is, are |
| `features a` / `boasts a` | has, includes |
| `plays a crucial role in` | influences, supports, drives |
| `a wide variety of` | various, multiple |

### Tier 2: Contextual Clichés (Flag when Clustered)
- *seamless, bespoke, empower, revolutionize, game-changer, ecosystem (non-biological), multifaceted, paramount, paramount importance, cutting-edge, state-of-the-art*.

### Tier 3: Repetitive Structural Boilerplate
- Repetitive transitions (*Moreover, Furthermore, Additionally, In conclusion*).
- Repetitive phrases (*the integration of, the implementation of, the optimization of* stacked 3+ times).

---

## 🛡️ Inviolable Preservation Rules

During any rewrite or humanization pass, the following elements **MUST NEVER BE ALTERED OR DROPPED**:
1. **Citation Tags**: All `{cite_XXX}` and `[VERIFY]` markers must be preserved exactly.
2. **LaTeX Math & Formulas**: Inline (`$...$`) and block (`$$...$$`) math must remain byte-for-byte identical.
3. **Data Tables & Code Fences**: Markdown tables and code snippets must not be reworded or deleted.
4. **URLs & Document Footnotes**: References and hyperlinks must remain unchanged.

---

## 🚫 Hard Ban on Em-Dashes (`—` / `–` / ` -- `)

Em-dashes are among the highest-weighted signals for automated AI detectors.
- **Rule:** The final text contains **ZERO** em-dashes (`—`), en-dashes (`–`), or double hyphens (` -- `).
- **Replacements:**
  1. Period (`.`) to create a fresh sentence.
  2. Comma (`,`) for a tight parenthetical aside.
  3. Colon (`:`) for introducing explanations or lists.
  4. True parentheses (`(...)`) for supplementary context.
