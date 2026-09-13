# AI Validation with Python

## Purpose

A hands-on Python learning repository for building foundational skills relevant to AI evaluation and validation workflows.

The exercises model common evaluation data such as experiment IDs, model settings, rubric scores, pass thresholds, and structured evaluation records.

## Learning Roadmap

- [x] Chapter 1 — Python Basics
- [ ] Working with files and CSV data
- [ ] Functions and reusable evaluation logic
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

## Skills Demonstrated

- Set up VS Code for use with GitHub repository and Codex
- Creating and using variables
- Working with strings, integers, floats, and booleans
- Accessing and updating lists
- Storing structured evaluation data in dictionaries
- Calculating total scores and percentages
- Applying a pass threshold with conditional logic
- Printing readable evaluation summaries

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
python3 exercises/01_python_basics/evaluation_result.py
```

To run every Chapter 1 exercise:

```bash
for file in exercises/01_python_basics/*.py; do
  python3 "$file"
done
```

## Evidence

`evaluation_result.py` produces a structured evaluation summary with rubric scores, a percentage, and a pass/fail decision.

Example result:

```text
Total: 24/25
Percentage: 96.0%
Decision: PASS
```

## Next Steps

Extend the project by extracting evaluation logic into functions.
