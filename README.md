# AI Validation with Python

## Purpose

A hands-on Python learning repository for building foundational skills relevant to AI evaluation and validation workflows.

The exercises model common evaluation data such as experiment IDs, model settings, rubric scores, pass thresholds, and structured evaluation records.

## Learning Roadmap

- [x] Chapter 1 — Python Basics
- [x] Chapter 2 — Python Functions
- [x] Chapter 3 — Python Loops
- [x] Chapter 4 — Files
- [ ] Working with CSV data
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

## Chapter 3 — Python Loops

Completed exercises cover:

- Iterating through lists with `for`
- Using `enumerate()` for numbered output and `range()` for repeated runs
- Counting passes, failures, generated combinations, and execution runs
- Calculating averages from a collection of scores
- Iterating through dictionaries with `.items()`
- Collecting failed test cases from evaluation results
- Processing batches of evaluation records and reporting aggregate results
- Organizing repeated observations by baseline and structured conditions

## Chapter 4 — Files

### Concepts

- Reading text files
- Writing files
- Append mode
- Relative file paths
- UTF-8 text handling
- Line-by-line processing
- Basic text parsing
- External input datasets
- Persistent evaluation results

### AI Validation Application

Refactored the batch evaluator so evaluation input is loaded from an external file and processed results are written to persistent output files. This separates validation data from evaluation logic and improves reproducibility.

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
- Using loops to process repeated evaluation observations
- Combining loops with reusable scoring functions
- Producing batch summaries and failure reports
- Loading validation inputs from external text files
- Writing reproducible evaluation reports to output files

## Repository Structure

```text
.
├── data/
│   ├── models.txt
│   ├── test_cases.txt
│   ├── scores.txt
│   └── evaluation_scores.txt
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
│   └── 03_loops/
│       ├── basic_iteration.py
│       ├── enumerate_test_cases.py
│       ├── range_runs.py
│       ├── calculate_result_summary.py
│       ├── calculate_average_score.py
│       ├── display_rubric_scores.py
│       ├── collect_failed_cases.py
│       ├── process_scores_with_functions.py
│       ├── model_test_combinations.py
│       ├── batch_evaluator.py
│       └── count_results_by_condition.py
│   └── 04_files/
│       ├── read_models.py
│       ├── read_models_lines.py
│       ├── write_simple_results.py
│       ├── append_evaluation_log.py
│       ├── load_test_cases.py
│       ├── save_results.py
│       ├── process_scores_file.py
│       └── file_driven_evaluator.py
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
python3 exercises/04_files/file_driven_evaluator.py
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

`file_driven_evaluator.py` loads evaluation scores from `data/evaluation_scores.txt`, processes each record, and writes an aggregate report to `results/evaluation_results.txt`.

Example result:

```text
T01 | 24/25 | 96.0% | PASS
T02 | 20/25 | 80.0% | PASS
T03 | 17/25 | 68.0% | FAIL

Total Evaluations: 5
Pass Rate: 80.0%
Average Percentage: 86.4%
```

## Next Steps

Extend the project by reading and writing CSV data.
