# AI Validation with Python

## Purpose

A hands-on Python learning repository for building foundational skills relevant to AI evaluation and validation workflows.

The exercises model common evaluation data such as experiment IDs, model settings, rubric scores, pass thresholds, and structured evaluation records.

## Learning Roadmap

- [x] Chapter 1 — Python Basics
- [x] Chapter 2 — Python Functions
- [ ] Working with files and CSV data
- [ ] Test cases and automated validation
- [ ] Data analysis and reporting

## Chapter 1 — Python Basics

Completed exercises cover:

- Variables for experiment metadata
- Core Python data types
- Lists of evaluated models
- Dictionaries and nested dictionaries
- Rubric-score calculations
- Pass/fail evaluation decisions

## Chapter 2 — Python Functions

Completed exercises cover:

- Defining and calling functions
- Passing individual values and lists as function arguments
- Returning calculated values and structured dictionaries
- Using default parameters for acceptance thresholds
- Composing small reusable functions into an evaluation workflow
- Separating calculation, result construction, and display responsibilities

## Skills Demonstrated

- Set up VS Code for use with GitHub repository and Codex
- Creating and using variables
- Working with strings, integers, floats, and booleans
- Accessing and updating lists
- Storing structured evaluation data in dictionaries
- Calculating total scores and percentages
- Applying a pass threshold with conditional logic
- Printing readable evaluation summaries
- Defining reusable functions with parameters and return values
- Using `sum()` to calculate totals from a score collection (list or dictionary)
- Building structured evaluation records from reusable functions

## Repository Structure

```text
.
├── exercises/
│   └── 01_python_basics/
│       ├── variables.py
│       ├── data_types.py
│       ├── lists.py
│       ├── dictionaries.py
│       ├── nested_dictionary.py
│       ├── rubric_calculation.py
│       └── evaluation_result.py
│   └── 02_functions/
│       ├── display_model_name.py
│       ├── calculate_score_percentage.py
│       ├── is_passing.py
│       ├── calculate_rubric_total.py
│       ├── create_evaluation_result.py
│       ├── evaluate_scores.py
│       └── evaluation_functions.py
├── docs/
│   └── engineering-log.md
├── requirements.txt
└── README.md
```

## Running the Exercises

Requirements:

- Python 3

Run an individual exercise from the repository root:

```bash
python3 exercises/02_functions/evaluation_functions.py
```

To run every exercise:

```bash
for file in exercises/*/*.py; do
  python3 "$file"
done
```

## Evidence

`evaluation_result.py` produces a structured evaluation summary with rubric scores, a percentage, and a pass/fail decision.

`evaluation_functions.py` refactors that workflow into reusable functions and returns a structured evaluation record containing metadata, named rubric scores, calculated results, and pass status.

Example result:

```text
Experiment: EXP-001
Total score: 24
Maximum score: 25
Percentage: 96.0%
Passed: True
```

## Next Steps

Extend the project by using loops.
