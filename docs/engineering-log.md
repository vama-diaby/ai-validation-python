## 2026-08-13 — Python Basics

### Objective

Build the Python language foundation required for automated AI validation.

### Work Completed

- Set up VS Code with Python, Codex, and a workspace connected to a GitHub repository
- Completed exercises for variables, core data types, lists, dictionaries, and nested dictionaries, rubric-score calculations, percentage conversion, and pass/fail decisions using an 80% threshold.


### Technical Decisions

- Leveraged previous exprience with using Codex in VS Code in tandem with ChatGPT


### Problems / Unexpected Findings

- No implementation errors were encountered while running the Chapter 1 exercises.


### Lessons Learned

- Codex as implementer, ChatGPT as reviewer with me is a solid approach to getting correct and fast achievements in using Python for AI vadlidation.
- Not much new learning in the Python language, given my developer experience with other languages

### Evidence Produced

- Seven runnable scripts in `exercises/01_python_basics/`.
- `evaluation_result.py` generates a structured result with a total score, percentage, and PASS/FAIL decision.
- The sample evaluation result records a score of 24/25 (96.0%) and a `PASS` decision.

### Next Steps

Proceed to Python Functions.

## 2026-09-13 — Python Functions

### Objective

Turn the Chapter 1 scoring workflow into reusable Python functions for a clearer and more maintainable evaluation process.

### Work Completed

- Created functions for displaying a model name, calculating score percentages, determining pass status, and calculating rubric totals.
- Created and called functions interactively in the Python terminal to confirm how imports and function arguments work.
- Combined reusable total, percentage, and threshold functions into a scoring workflow.
- Refactored the evaluation calculator to create a structured result containing experiment metadata, named rubric scores, calculated results, and pass status.
- Reviewed and updated functions created by Codex, including changing rubric totals from five individual parameters to a list of scores.

### Technical Decisions

- Kept calculation, threshold, result-construction, and display responsibilities in separate functions.
- Used a dictionary of named rubric scores so each score remains identifiable in the final evaluation record.

### Problems / Unexpected Findings

- An interactive Python session retained an earlier version of `calculate_rubric_total` after the source file changed. Restarting the interpreter or reloading the module was required to use the updated function signature.

### Lessons Learned

- Function parameters and return values make repeated evaluation logic easier to reuse and test.
- Interactive terminal use is useful for learning, but imported modules stay in memory until explicitly reloaded or the session is restarted.
- Reviewing and updating generated code is necessary to verify that its interfaces and data structures match the intended evaluation design.

### Evidence Produced

- Seven runnable exercises in `exercises/02_functions/`.
- `evaluation_functions.py` provides reusable scoring functions and produces an evaluation result for `EXP-001` with a score of 24/25 (96.0%) and `passed: True`.
- The README now documents the completed Python Functions lesson and its runnable exercises.

### Next Steps

Proceed to working with loops.
