from pathlib import Path


log_path = Path("results/evaluation.log")
log_path.parent.mkdir(exist_ok=True)


def append_log_entry(message):
    with log_path.open("a", encoding="utf-8") as log_file:
        log_file.write(message + "\n")


append_log_entry("Started T01")
append_log_entry("Completed T01")
append_log_entry("Started T02")
append_log_entry("Completed T02")
