# CLAUDE.md

This file provides guidance for Claude Code when working with this project.

## Project Overview

This is a spec-driven Python console application that implements a todo list manager. The project follows Spec-Kit Plus (SDD) methodology where all code originates from approved specifications.

## Development Workflow

1. **Create/Update Specification** (`/sp.specify`)
   - Define feature requirements in `specs/001-todo-cli/spec.md`
   - Document user stories with priorities (P1, P2, etc.)

2. **Clarify Ambiguities** (`/sp.clarify`)
   - Resolve any unclear requirements before planning
   - Updates are recorded in the spec's Clarifications section

3. **Create Implementation Plan** (`/sp.plan`)
   - Architecture decisions with trade-offs
   - Module structure and data model design
   - Saved to `specs/001-todo-cli/plan.md`

4. **Generate Tasks** (`/sp.tasks`)
   - Actionable task breakdown organized by user story
   - Saved to `specs/001-todo-cli/tasks.md`

5. **Implement** (`/sp.implement`)
   - Execute tasks following the plan
   - All code goes in `src/` directory

## Code Standards

### Python Conventions

- **PEP 8** compliance required
- Use type hints for all function signatures
- Dataclasses for data models
- Clear, descriptive names

### Module Organization

```
src/
├── models.py        # Data classes (Task)
├── todo_service.py  # Business logic (CRUD operations)
├── cli.py           # Console interface (menu, input handling)
└── main.py          # Entry point
```

### Key Principles

- **Separation of concerns**: Models, service, and CLI are separate
- **No magic values**: Use constants or comments for special values
- **Error handling**: User-friendly messages, re-prompt on invalid input
- **No external dependencies**: Standard library only

## Technical Constraints

- Python 3.13+ only
- In-memory storage (no files, no database)
- UV-managed virtual environment
- No third-party runtime dependencies

## Success Criteria

- All 5 features work correctly via console interaction
- Application runs without errors in fresh UV environment
- Specifications fully describe implemented behavior
- Code passes manual review for cleanliness
