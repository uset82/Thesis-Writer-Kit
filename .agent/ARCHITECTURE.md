# Thesis Writer Kit - Architecture

> Complete system documentation for AI-powered thesis research and writing.

---

## System Overview

Thesis Writer Kit is a modular AI assistant framework for academic research and writing. It combines specialized agents, domain skills, and workflow automations to produce authentic, citation-verified thesis drafts.

```
┌─────────────────────────────────────────────────────────────────┐
│                      THESIS WRITER KIT                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │   AGENTS    │  │   SKILLS    │  │  WORKFLOWS  │             │
│  │  (5 total)  │  │  (6 total)  │  │  (6 total)  │             │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘             │
│         │                │                │                     │
│         └────────────────┼────────────────┘                     │
│                          ▼                                      │
│              ┌───────────────────────┐                          │
│              │     OPENDRAFT         │                          │
│              │   Research Engine     │                          │
│              │   (19 Sub-Agents)     │                          │
│              └───────────────────────┘                          │
│                          │                                      │
│                          ▼                                      │
│              ┌───────────────────────┐                          │
│              │   Academic Databases  │                          │
│              │   200M+ Papers        │                          │
│              └───────────────────────┘                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Directory Structure

```
thesiswriter/
│
├── README.md                    # Project overview
├── RUN.md                       # Quick start guide
├── LICENSE                      # MIT License
│
├── .agent/                      # AI Agent Framework
│   ├── ARCHITECTURE.md          # This file
│   │
│   ├── agents/                  # 5 Specialist Agents
│   │   ├── research-agent.md    # Literature search
│   │   ├── writing-agent.md     # Academic drafting
│   │   ├── citation-agent.md    # Citation verification
│   │   ├── editor-agent.md      # Grammar & style
│   │   └── humanizer-agent.md   # AI detection bypass
│   │
│   ├── skills/                  # 6 Domain Skills
│   │   ├── academic-writing/    # PEEL, thesis structure
│   │   ├── citation-management/ # APA 7, DOI verification
│   │   ├── thesis-structure/    # Chapters, argument maps
│   │   ├── ai-bypass/           # Stealth strategies
│   │   ├── research-methods/    # Literature search
│   │   └── harper/              # Grammar checking
│   │
│   ├── workflows/               # 6 Slash Commands
│   │   ├── research.md          # /research
│   │   ├── draft.md             # /draft
│   │   ├── cite.md              # /cite
│   │   ├── humanize.md          # /humanize
│   │   ├── export.md            # /export
│   │   └── status.md            # /status
│   │
│   ├── rules/                   # Workspace Rules
│   │   └── RULES.md             # Default behavior
│   │
│   ├── config/                  # Configuration
│   │   └── thesis.yaml          # Thesis settings
│   │
│   └── opendraft/               # Research Engine
│       ├── engine/              # Python backend
│       ├── docs/                # Engine documentation
│       └── README.md            # Engine overview
│
├── Papers/                      # Source materials
│
├── chatgpt_research/            # Research notes
│
└── drafts/                      # Generated drafts
```

---

## Agent Architecture

### Agent Pipeline

```
Research → Writing → Citation → Editing → Humanizing
   │          │          │          │          │
   ▼          ▼          ▼          ▼          ▼
Sources    Draft     Verified    Polished   Authentic
                     Citations    Draft      Output
```

### Agent Responsibilities

| Agent | Input | Output | Skills Used |
|-------|-------|--------|-------------|
| research-agent | Topic/RQ | Annotated sources | research-methods, citation-management |
| writing-agent | Sources + outline | Section draft | academic-writing, thesis-structure |
| citation-agent | Draft | Verified citations | citation-management |
| editor-agent | Draft | Polished prose | academic-writing, harper |
| humanizer-agent | Draft | Authentic text | ai-bypass |

### Agent Communication

Agents communicate via:
1. **File handoff**: Output files become input for next agent
2. **Context passing**: Shared thesis configuration
3. **Workflow orchestration**: `/draft` invokes multiple agents

---

## Skills System

### Skill Structure

Each skill follows this format:

```
skills/
└── skill-name/
    ├── SKILL.md           # Main documentation
    ├── sections/          # Detailed guides (optional)
    ├── examples/          # Reference samples (optional)
    └── scripts/           # Helper utilities (optional)
```

### Skill Mapping

| Skill | Used By Agents | Purpose |
|-------|----------------|---------|
| academic-writing | writing-agent, editor-agent | Prose quality |
| citation-management | research-agent, citation-agent | APA 7 format |
| thesis-structure | writing-agent | Chapter organization |
| ai-bypass | humanizer-agent | Detection avoidance |
| research-methods | research-agent | Source finding |
| harper | editor-agent | Grammar checking |

---

## Workflow System

### Workflow Execution

```
User Command → Parse Options → Execute Steps → Output

Example:
/draft introduction --words 600
    │
    ├─► Load thesis config
    ├─► Read sources
    ├─► Invoke writing-agent
    ├─► Apply PEEL structure
    ├─► Generate draft
    └─► Output with prompts
```

### Workflow Dependencies

```
/research ──► /draft ──► /cite ──► /humanize ──► /export
                                       │
                                       └──► /status
```

---

## OpenDraft Engine

### Engine Architecture

OpenDraft uses 19 specialized sub-agents:

```
┌────────────────────────────────────────────────────────┐
│                    OPENDRAFT ENGINE                    │
├────────────────────────────────────────────────────────┤
│                                                        │
│  📚 RESEARCH PHASE                                     │
│  ├── Query Formulator                                  │
│  ├── Database Searcher                                 │
│  ├── Source Screener                                   │
│  └── Annotator                                         │
│                                                        │
│  🏗️ STRUCTURE PHASE                                    │
│  ├── Outline Generator                                 │
│  ├── Argument Mapper                                   │
│  └── Section Planner                                   │
│                                                        │
│  ✍️ WRITING PHASE                                      │
│  ├── Introduction Writer                               │
│  ├── Literature Reviewer                               │
│  ├── Methodology Writer                                │
│  ├── Analysis Writer                                   │
│  └── Conclusion Writer                                 │
│                                                        │
│  🔍 CITATION PHASE                                     │
│  ├── Citation Verifier (CrossRef)                      │
│  ├── DOI Resolver                                      │
│  └── Bibliography Formatter                            │
│                                                        │
│  ✨ POLISH PHASE                                       │
│  ├── Grammar Checker                                   │
│  ├── Style Refiner                                     │
│  └── Humanizer                                         │
│                                                        │
│  📄 EXPORT PHASE                                       │
│  └── Format Converter (PDF, DOCX, LaTeX)               │
│                                                        │
└────────────────────────────────────────────────────────┘
```

### Engine Data Flow

```
Topic/RQ
    │
    ▼
┌──────────────────┐
│  OpenAlex API    │──► 200M+ papers
│  CrossRef API    │──► DOI verification
│  Semantic Scholar│──► AI/CS papers
└──────────────────┘
    │
    ▼
Screened Sources
    │
    ▼
Thesis Outline
    │
    ▼
Section Drafts
    │
    ▼
Verified Citations
    │
    ▼
Polished Output
    │
    ▼
PDF / DOCX / LaTeX
```

---

## Configuration

### Thesis Configuration (config/thesis.yaml)

```yaml
# Thesis Configuration
thesis:
  title: "Your Thesis Title"
  research_question: "Your research question?"
  
  # Structure
  level: master  # bachelor, master, phd
  word_limit: 4000
  citation_style: apa7
  
  # Sections
  sections:
    - name: introduction
      target_words: 600
    - name: theoretical_framework
      target_words: 600
    - name: case_study
      target_words: 800
    - name: analysis
      target_words: 1000
    - name: recommendations
      target_words: 800
    - name: conclusion
      target_words: 400
  
  # Output
  output:
    format: pdf
    template: academic
```

---

## Quality Framework

### Writing Quality Layers

```
Layer 1: Structure
├── Thesis statement clear
├── Sections follow template
└── Arguments mapped to evidence

Layer 2: Content
├── Claims supported by citations
├── PEEL paragraphs used
└── Analysis depth appropriate

Layer 3: Language
├── Grammar correct
├── Academic register
└── Sentence variety

Layer 4: Authenticity
├── No AI markers
├── Specifics throughout
└── Human voice present

Layer 5: Citations
├── APA 7 compliant
├── DOIs verified
└── No patchwriting
```

### Quality Checkpoints

| Checkpoint | When | Agent/Workflow |
|------------|------|----------------|
| Source verification | After research | citation-agent |
| Structure check | After outline | writing-agent |
| Citation verify | After draft | /cite |
| AI detection | Before export | /humanize |
| Final review | Before submit | /status |

---

## Integration Points

### AI Assistant Integration

Works with:
- **Cursor** (Claude, GPT-4)
- **VS Code Copilot**
- **GitHub Copilot Chat**
- **Windsurf**

### External APIs

| Service | Purpose | Authentication |
|---------|---------|----------------|
| Google Gemini | LLM Backend | API Key |
| OpenAlex | Paper search | Free |
| CrossRef | DOI verification | Free |
| Semantic Scholar | Paper search | Free |

---

## Extension Points

### Adding New Agents

1. Create `agents/new-agent.md`
2. Define: name, description, tools, skills
3. Write agent instructions
4. Update workflows to use agent

### Adding New Skills

1. Create `skills/new-skill/SKILL.md`
2. Document the domain knowledge
3. Map to relevant agents
4. Add examples if needed

### Adding New Workflows

1. Create `workflows/command.md`
2. Define: usage, options, steps
3. Specify agent coordination
4. Add integration points

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Citations not verifying | Check DOI format, try CrossRef directly |
| AI detection flagged | Run /humanize --aggressive |
| Word count off | Adjust section targets in config |
| Export fails | Check Pandoc installation |

### Debug Mode

Enable verbose output:
```bash
python -m opendraft.cli "topic" --verbose
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01 | Initial Antigravity-style structure |

---

## License

MIT © 2026
