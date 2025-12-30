# Todo Console App Constitution

## Core Principles

### I. Spec-Driven Development
All code must originate from approved specifications. Every feature must be defined in specifications before implementation. Each change must produce a new spec entry in the specs history folder.

### II. Simplicity and Clarity
Code should be accessible for beginner-to-intermediate Python developers. Prioritize readability over clever optimizations. Clear, descriptive naming for all variables, functions, and classes.

### III. Correctness of Business Logic
Task lifecycle must behave predictably. Edge cases must be handled gracefully. No hidden state or surprising side effects.

### IV. Maintainability
Clean, readable, modular Python code. Functions and classes must have clear, single responsibilities. No duplicate logic across functions. No hard-coded magic values without explanation.

### V. Deterministic Behavior
No hidden state beyond in-memory data structures. Same inputs always produce same outputs. No external side effects.

## Functional Requirements

The application must support five core features:

1. **Add Task** – Create a task with unique ID, title, description, and default incomplete status
2. **Delete Task** – Remove a task using its unique ID
3. **Update Task** – Modify title and/or description of an existing task
4. **View Task List** – Display all tasks with ID, title, description, and completion status
5. **Mark as Complete** – Toggle task completion state (complete/incomplete)

## Technical Constraints

- **Language**: Python 3.13+
- **Environment**: UV-managed virtual environment
- **Architecture**: Console-based application only
- **Storage**: In-memory data structures (list or dictionary)
- **Dependencies**: Standard library only (no third-party runtime dependencies)

## Code Standards

### PEP 8 Compliance
All Python code must follow PEP 8 conventions.

### Separation of Concerns
- Clear separation between user input, business logic, and output formatting
- Graceful handling of invalid user input

### No Magic Values
All magic values must be explained with constants or comments.

## Project Structure

```
todo-console-app/
├── .specify/
│   ├── memory/
│   │   └── constitution.md    (this file)
│   ├── templates/
│   └── scripts/
├── src/
│   └── (Python source code)
├── specs/
│   └── (spec evolution files)
├── history/
│   ├── prompts/
│   └── adr/
├── README.md
└── CLAUDE.md
```

## Documentation Standards

### README.md
Must include:
- Project overview
- Setup instructions using UV
- How to run the console app
- Example usage flow

### CLAUDE.md
Must clearly define:
- How Claude Code should generate specs
- How implementations must follow specs strictly

## Success Criteria

- All five basic-level features work correctly via console interaction
- Application runs without errors in a fresh UV environment
- Specifications fully describe the implemented behavior
- Code passes manual review for cleanliness and readability
- Project structure exactly matches defined deliverables

## Governance

This constitution supersedes all other development practices. Amendments require documentation and approval.

**Version**: 1.0.0 | **Ratified**: 2025-12-30 | **Last Amended**: 2025-12-30
