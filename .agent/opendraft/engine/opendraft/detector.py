#!/usr/bin/env python3
"""
ABOUTME: Python bridge to the avoid-ai-writing deterministic scoring and preservation validation engine.
ABOUTME: Executes tools/detector/patterns.js and tools/detector/validate.js via Node.js.
"""

import json
import os
import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, cast


def _get_detector_dir() -> Path:
    """Find tools/detector directory relative to this file or workspace."""
    # Try relative to this file
    current = Path(__file__).resolve().parent
    # Check parent workspace directories
    candidates = [
        current.parent.parent.parent.parent / "tools" / "detector",
        current.parent.parent.parent / "tools" / "detector",
        Path.cwd() / "tools" / "detector",
        Path("d:/Proyectos/thesiswriter/tools/detector")
    ]
    for c in candidates:
        if (c / "patterns.js").exists():
            return c
    raise FileNotFoundError("Could not locate tools/detector/patterns.js")


def is_node_available() -> bool:
    """Check if node runtime is available on the system PATH."""
    return shutil.which("node") is not None


@dataclass
class AuditIssue:
    type: str
    text: str
    severity: str
    start: Optional[int] = None
    end: Optional[int] = None


@dataclass
class AuditResult:
    score: int
    label: str
    document_classification: str
    issues: List[Dict[str, Any]]
    stats: Dict[str, Any]
    probabilities: Dict[str, float]
    highlights: List[Dict[str, Any]] = field(default_factory=list)

    @property
    def is_clean(self) -> bool:
        return self.score <= 15


def analyze_text(text: str, context_mode: str = "general") -> AuditResult:
    """
    Run deterministic AI pattern detection on text.

    Args:
        text: String content to analyze.
        context_mode: 'general' or 'technical' (technical suppresses title-case header flags).

    Returns:
        AuditResult with score (0-100), classification, and list of specific issues.
    """
    if not is_node_available():
        raise RuntimeError("Node.js runtime is required to run the deterministic pattern engine.")

    detector_dir = _get_detector_dir()
    patterns_js = (detector_dir / "patterns.js").resolve().as_posix()

    node_script = f"""
    const AIDetector = require('{patterns_js}');
    let input = '';
    process.stdin.setEncoding('utf8');
    process.stdin.on('data', chunk => {{ input += chunk; }});
    process.stdin.on('end', () => {{
        const result = AIDetector.analyzeText(input, {{ contextMode: '{context_mode}' }});
        process.stdout.write(JSON.stringify(result));
    }});
    """

    proc = subprocess.run(
        ["node", "-e", node_script],
        input=text,
        text=True,
        encoding="utf-8",
        capture_output=True,
        check=True
    )

    data = json.loads(proc.stdout)
    return AuditResult(
        score=data.get("score", 0),
        label=data.get("label", "Unknown"),
        document_classification=data.get("document_classification", "UNSCORED"),
        issues=data.get("issues", []),
        stats=data.get("stats", {}),
        probabilities=data.get("class_probabilities", {}),
        highlights=data.get("highlight_sentence_for_ai", [])
    )


def validate_preservation(original_text: str, rewritten_text: str) -> Dict[str, Any]:
    """
    Verify that an AI rewrite preserved code, frontmatter, citations, formulas, and tables intact.

    Returns:
        Dict with 'ok' (bool), 'errors' (list), and 'warnings' (list).
    """
    if not is_node_available():
        raise RuntimeError("Node.js runtime is required to run the preservation validator.")

    detector_dir = _get_detector_dir()
    validate_js = (detector_dir / "validate.js").resolve().as_posix()

    node_script = f"""
    const {{ validate }} = require('{validate_js}');
    let input = '';
    process.stdin.setEncoding('utf8');
    process.stdin.on('data', chunk => {{ input += chunk; }});
    process.stdin.on('end', () => {{
        const payload = JSON.parse(input);
        const result = validate(payload.original, payload.rewritten);
        process.stdout.write(JSON.stringify(result));
    }});
    """

    payload = json.dumps({"original": original_text, "rewritten": rewritten_text})
    proc = subprocess.run(
        ["node", "-e", node_script],
        input=payload,
        text=True,
        encoding="utf-8",
        capture_output=True,
        check=True
    )

    return cast(Dict[str, Any], json.loads(proc.stdout))


def format_cli_report(result: AuditResult) -> str:
    """Format an audit result for clean terminal display."""
    lines: List[str] = []
    lines.append("=" * 60)
    lines.append(f" AI AUDIT SCORECARD: {result.score}/100 [{result.label.upper()}]")
    lines.append(f" Classification: {result.document_classification}")
    if result.probabilities:
        probs = ", ".join(f"{k}: {v*100:.1f}%" for k, v in result.probabilities.items())
        lines.append(f" Probabilities: {probs}")
    lines.append("=" * 60)

    if not result.issues:
        lines.append("\n [OK] No AI writing patterns detected! Prose appears human-authored.\n")
    else:
        lines.append(f"\n Detected {len(result.issues)} AI pattern tell(s):\n")
        for idx, issue in enumerate(result.issues[:15], 1):
            itype = issue.get("type", "unknown")
            text = issue.get("text", "")
            sev = issue.get("severity", "medium")
            lines.append(f"  {idx}. [{sev.upper()}] {itype}: \"{text}\"")
        if len(result.issues) > 15:
            lines.append(f"  ... and {len(result.issues) - 15} more issues.")

    lines.append("\n" + "=" * 60)
    return "\n".join(lines)
