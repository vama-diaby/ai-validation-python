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

## 2026-08-18 — Python Loops

### Objective

Learn to use Python iteration to process multiple AI-validation records consistently and replace repeated manual processing with reusable batch logic.

### Work Completed

- Practiced `for` loops with model lists and test-case collections.
- Practiced `range()` for sequential run numbers and repeated executions.
- Practiced `enumerate()` for numbered test-case output.
- Iterated through lists and dictionaries, including dictionary `.items()`.
- Implemented counters and accumulators for pass/fail totals, combinations, and average scores.
- Used conditional logic inside loops to identify failed evaluations.
- Combined Chapter 2 scoring functions with loops to evaluate multiple scores consistently.
- Processed multiple structured evaluation records in a batch.
- Calculated aggregate pass/fail metrics, including pass rate and average percentage.
- Created a batch AI evaluation processor and a separate condition-counting exercise for baseline and structured observations.

### Technical / Methodological Decisions

- Used `for` loops for known evaluation collections.
- Kept scoring logic inside reusable functions rather than duplicating it inside loops.
- Preserved individual evaluation results before calculating aggregate statistics.
- Recorded failed test cases separately for investigation.
- Used an explicit 80% pass/fail threshold consistently across all cases.

### Problems / Unexpected Findings

- No runtime errors occurred in the completed loop exercises.
- `range()` uses an exclusive upper bound, so `range(1, 6)` was required to produce runs 1 through 5 and `range(1, 4)` was required for three repetitions.
- Nested loops make the number of executions grow quickly; the program counted generated executions rather than manually entering the expected total.

### Lessons Learned

- Loops turn one-off evaluation logic into repeatable processing for lists of models, test cases, and evaluation records.
- Counters and accumulators allow totals, averages, pass rates, and failure lists to be derived from the data.
- Nested loops are useful for experimental combinations such as model × test case × run.
- Functions and loops have complementary responsibilities: functions perform a single calculation while loops apply it across many observations.

### Evidence Produced

- Loop practice scripts in `exercises/03_loops/`.
- Dictionary iteration and nested-loop exercises.
- `batch_evaluator.py`, which produces aggregate validation output and a failed-case report.
- `count_results_by_condition.py`, which counts baseline and structured observations.
- Git commit history and an updated README.

### Next Steps

Proceed to Python Files so evaluation inputs and outputs no longer need to be hardcoded directly inside Python scripts.

## 2026-08-19 — Python Files

### Objective

Learn to read and write external files so AI-validation datasets and results can be stored independently from Python source code and preserved as reproducible evidence.

### Work Completed

- Practiced opening and reading text files with `.read()`, `.readlines()`, and `.readline()`.
- Iterated directly through file contents and used `.strip()` to normalize input lines.
- Practiced writing and appending to files.
- Used UTF-8 encoding explicitly.
- Created reusable file-loading and file-writing functions.
- Moved evaluation inputs outside Python source code.
- Wrote processed validation results to external files.
- Created a file-driven AI validation processor.
- Used Codex successfully to implement scoped exercises, then reviewed the code and verified the generated output against the required results.

### Technical / Methodological Decisions

- Used `with open(...)` so files are closed automatically.
- Used UTF-8 for text files.
- Separated input data from generated results.
- Preserved raw input files rather than modifying them during processing.
- Used relative project paths rather than machine-specific absolute paths.
- Kept file I/O responsibilities separate from scoring logic.
- Added `results/` to `.gitignore` so generated reports do not become version-controlled source artifacts.

### Problems / Unexpected Findings

- Reading a file with `.readlines()` returns a list, while direct iteration yields one line at a time from the file object.
- Input lines include newline characters; `.strip()` was required before parsing and displaying values.
- Blank lines in `test_cases.txt` would otherwise fail the delimiter split, so the loader uses `continue` to ignore them.
- Running the append-mode logging script twice produced duplicate entries, demonstrating that append mode preserves existing content instead of replacing it.
- Generated reports are reproducible runtime artifacts, so they were kept out of Git while source datasets and scripts were committed.

### Lessons Learned

- Files provide persistence beyond a single Python run and make evaluation inputs and outputs inspectable.
- Relative paths keep the exercises portable when run from the repository root.
- Separating data from logic makes the evaluator easier to update without changing the scoring code.
- Preserving raw source data and failed results supports reproducibility and later investigation.
- Reading, writing, and appending are distinct operations with different effects on existing file contents.
- Codex can accelerate implementation when requirements are specific, while review and execution checks ensure that the resulting code matches the intended workflow.

### Evidence Produced

- File-reading and file-writing exercises in `exercises/04_files/`.
- External evaluation datasets in `data/`.
- A file-driven evaluator that writes batch results and preserves failed cases.
- An append-mode execution log demonstrating duplicate logging behavior.
- Git commit history and an updated README.

### Next Steps

Proceed to CSV so tabular evaluation datasets can be represented and processed using a standard structured format instead of custom delimiter parsing.
