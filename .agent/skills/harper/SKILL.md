# Harper Grammar Checker Skill

> **Type**: Grammar & Style Checker
> **Source**: https://github.com/automattic/harper
> **Location**: `.agent/opendraft/harper/`

---

## Overview

Harper is an offline, privacy-first grammar checker written in Rust. It is:
- **Fast**: Milliseconds to lint a document
- **Private**: No data sent to external servers
- **Lightweight**: 1/50th of LanguageTool's memory footprint

---

## Installation (Choose One)

### Option 1: VS Code Extension (Recommended)

1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "Harper"
4. Install the official Harper extension
5. Done! Harper will automatically check your markdown files.

### Option 2: Build from Source (Requires Rust)

**Prerequisites**: Install Rust from https://rustup.rs/

```bash
cd .agent/opendraft/harper
cargo build --release -p harper-cli
```

**Usage**:
```bash
./target/release/harper-cli lint drafts/01_introduction.md
```

---

## Integration with Agent Workflow

### Pre-Writing (Phase 2)

After drafting a section, run Harper to check grammar:

```bash
harper-cli lint drafts/01_introduction.md
```

### Post-Writing (Phase 3)

Verify all sections pass grammar check before submission:

```bash
harper-cli lint drafts/*.md
```

---

## Rules to Enforce

Harper will catch:
- [x] Subject-verb agreement
- [x] Article errors ("a" vs "an")
- [x] Sentence structure issues
- [x] Repeated words
- [x] Punctuation errors

**Note**: Harper does NOT catch:
- AI marker words (use AIbypass.md for this)
- Style issues (use thesis_writing_strategy.md)

---

## Quick Commands

| Task | Command |
|------|---------|
| Build CLI | `cargo build --release -p harper-cli` |
| Lint file | `harper-cli lint <file.md>` |
| Lint all drafts | `harper-cli lint drafts/*.md` |

---

## References

- [Harper GitHub](https://github.com/automattic/harper)
- [Harper Website](https://writewithharper.com)
- [VS Code Integration](https://writewithharper.com/docs/integrations/visual-studio-code)
