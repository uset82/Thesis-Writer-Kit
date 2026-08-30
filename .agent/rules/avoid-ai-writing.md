# Workspace Rule: Avoid AI Writing Patterns

> Automated writing constraints to ensure all generated prose avoids machine tells and reads as genuine academic research.

---

## 🚫 Hard Constraints for Assistant Output

1. **NO EM-DASHES (`—` / `–` / ` -- `):**
   - Treat em-dashes as strictly prohibited in final text.
   - Replace with commas, periods, colons, or parentheticals.

2. **NO HIGH-FREQUENCY AI VOCABULARY:**
   - Eradicate: *delve, landscape, testament to, tapestry, pivotal, underscore, vibrant, nestled in, watershed moment, foster, garner*.

3. **NO COPULA AVOIDANCE:**
   - Use direct, natural verbs ("is", "are", "has", "includes") instead of "serves as", "stands as", "boasts".

4. **NO CHATBOT PREAMBLES OR META-COMMENTARY:**
   - Zero tolerance for "Okay, I will write...", "Here's the plan...", or conversational conclusion cheerleading.

5. **NO INVALID CITATION PLACEHOLDERS:**
   - Never write `{cite_MISSING: ...}`. Rephrase or verify references using standard `{cite_XXX}` keys.

6. **PRESERVATION GUARANTEE:**
   - Never alter citations, LaTeX formulas (`$...$`), code blocks, or data tables when refining prose.
