#!/usr/bin/env python3
"""
ABOUTME: YourWrite integration for OpenDraft engine.
ABOUTME: Detects and eliminates AI-writing patterns, performs voice calibration, and produces authentic human academic prose.
"""

import os
import re
import sys
from pathlib import Path
from typing import Optional

try:
    import google.generativeai as genai
except ImportError:
    genai = None

from config import get_config

SYSTEM_PROMPT = """You are an expert academic writing editor that identifies and removes signs of AI-generated text to make writing sound authentic, rigorous, and human. This guide is based on 33 empirical patterns from Wikipedia's WikiProject AI Cleanup.

## Your Task

When given text to humanize:
1. **Identify AI patterns** - Scan for the 33 patterns listed below.
2. **Rewrite, don't delete** - Replace AI-isms with natural alternatives while preserving the core arguments, depth, and citation keys ({cite_XXX}).
3. **Preserve meaning & citations** - Keep the core message and all {cite_XXX} references intact. Never use {cite_MISSING}.
4. **Match the voice** - When an author's writing sample is provided, calibrate sentence lengths, tone, and rhythm to match.
5. **ZERO EM-DASHES** - Never use em-dashes (—) or en-dashes (–). Replace with commas, periods, colons, or parentheticals.

## 33 AI Patterns to Eliminate:

### Content & Framing
1. Undue emphasis on significance/legacy ("stands as a testament", "pivotal moment", "evolving landscape").
2. Notability inflation ("independent coverage", "leading experts argue").
3. Superficial present-participle (-ing) endings ("highlighting the importance...", "ensuring...").
4. Promotional language ("boasts", "vibrant", "groundbreaking", "breathtaking").
5. Vague attributions & weasel words ("industry reports suggest", "observers believe").
6. Formulaic "Challenges & Future Outlook" outline structures.

### Language & Grammar
7. High-frequency AI words (delve, landscape, testament, tapestry, pivotal, underscore, align with, crucial, foster, garner).
8. Copula avoidance ("serves as", "stands as" -> replace with "is", "are", "has").
9. Negative parallelisms ("Not only X, but Y", "It's not just about X, it's Y").
10. Rule-of-three list packing.
11. Elegant variation (unnatural synonym cycling).
12. False ranges ("from the birth of stars to the dance of molecules").
13. Passive voice & subjectless fragments.

### Style & Punctuation
14. EM-DASHES AND EN-DASHES: Treat as a hard ban. Scan and remove every '—' and '–'.
15. Overuse of boldface in narrative body text.
16. Inline-header vertical bullet lists in place of continuous academic prose.
17. Title case in section subheadings.
18. Emojis and decorative icons.
19. Curly quotation marks (normalize to straight quotes).

### Communication & Meta
20. Collaborative chatbot artifacts ("I hope this helps", "Let's explore", "Here is...").
21. Knowledge-cutoff disclaimers ("as of my last update").
22. Sycophantic or overly eager tone.
23. Wordy filler phrases ("In order to" -> "To", "Due to the fact that" -> "Because").
24. Excessive hedging ("could potentially possibly").
25. Generic uplifting conclusions.
26. Predicate-position hyphenated word pairs.
27. Persuasive authority tropes ("At its core", "What really matters").
28. Signposting announcements ("Let's dive into", "Now let's examine").
29. Fragmented one-line rhetorical headers.
30. Diff-anchored commentary.
31. Manufactured punchlines & staccato drama.
32. Aphorism formulas ("X is the currency of Y").
33. Conversational rhetorical openers ("Honestly?", "Real talk").

## Output Instruction:
Output ONLY the final humanized text with no conversational preambles, meta-commentary, or markdown code fences unless the original had code.
"""


def clean_formatting_artifacts(text: str) -> str:
    """Post-processing filter to strip out remaining em-dashes and formatting artifacts."""
    # Replace em-dashes and en-dashes
    cleaned = text.replace("—", ", ").replace("–", "-")
    cleaned = re.sub(r'\s+--\s+', ', ', cleaned)
    # Remove any leaked cite_MISSING tags
    cleaned = re.sub(r'\{cite_MISSING:[^}]*\}', '', cleaned)
    return cleaned


def humanize_text(
    text: str,
    api_key: Optional[str] = None,
    writing_sample: Optional[str] = None,
    model_name: Optional[str] = None,
) -> str:
    """
    Humanize text by applying the 33 anti-AI patterns and voice calibration using Gemini.

    Args:
        text: The draft text to humanize.
        api_key: Optional Google API key (falls back to config/env).
        writing_sample: Optional reference sample of the author's writing.
        model_name: Gemini model identifier.

    Returns:
        Humanized text string.
    """
    cfg = get_config()
    key = api_key or cfg.google_api_key or os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

    if not key:
        raise ValueError("Google API Key is required for humanization. Set GOOGLE_API_KEY in environment or .env.")

    if not genai:
        raise ImportError("google-generativeai package is required. Install via `pip install google-generativeai`.")

    genai.configure(api_key=key)

    chosen_model = model_name or os.getenv("GEMINI_HUMANIZER_MODEL", "gemini-2.5-flash")

    # Build prompt
    prompt_parts = [SYSTEM_PROMPT]

    if writing_sample:
        prompt_parts.append(
            f"\n\n## Author Writing Sample (Calibrate tone, sentence rhythm, and style to match this):\n\n{writing_sample}"
        )

    prompt_parts.append(f"\n\n## Text to Humanize:\n\n{text}")

    full_prompt = "\n".join(prompt_parts)

    try:
        model = genai.GenerativeModel(
            model_name=chosen_model,
            generation_config=genai.GenerationConfig(temperature=0.6, top_p=0.9)
        )
        response = model.generate_content(full_prompt)
        raw_output = response.text.strip()
        return clean_formatting_artifacts(raw_output)
    except Exception as e:
        # Fallback to gemini-1.5-flash if 2.5-flash is unavailable
        if chosen_model != "gemini-1.5-flash":
            try:
                fallback_model = genai.GenerativeModel("gemini-1.5-flash")
                response = fallback_model.generate_content(full_prompt)
                return clean_formatting_artifacts(response.text.strip())
            except Exception:
                pass
        raise RuntimeError(f"Humanization request failed: {e}")


def main():
    """CLI entrypoint for standalone humanization."""
    import argparse

    parser = argparse.ArgumentParser(description="YourWrite Humanizer - Remove AI patterns from text.")
    parser.add_argument("input", nargs="?", help="Input text file to humanize (or pass --text)")
    parser.add_argument("--text", help="Direct text string to humanize")
    parser.add_argument("--sample", help="Path to author writing sample file for voice calibration")
    parser.add_argument("--output", "-o", help="Output file path (default: prints to stdout)")
    parser.add_argument("--model", default="gemini-2.5-flash", help="Gemini model to use")

    args = parser.parse_args()

    content = ""
    if args.text:
        content = args.text
    elif args.input:
        in_path = Path(args.input)
        if not in_path.exists():
            print(f"Error: File '{args.input}' not found.", file=sys.stderr)
            sys.exit(1)
        content = in_path.read_text(encoding="utf-8")
    else:
        # Read from stdin if piped
        if not sys.stdin.isatty():
            content = sys.stdin.read()
        else:
            parser.print_help()
            sys.exit(1)

    sample_content = None
    if args.sample:
        sample_path = Path(args.sample)
        if sample_path.exists():
            sample_content = sample_path.read_text(encoding="utf-8")

    try:
        result = humanize_text(content, writing_sample=sample_content, model_name=args.model)
        if args.output:
            out_path = Path(args.output)
            out_path.write_text(result, encoding="utf-8")
            print(f"Saved humanized output to: {args.output}")
        else:
            print(result)
    except Exception as err:
        print(f"Error during humanization: {err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
