# Daily Schedule Tracker 🐾

A command-line Python application for managing daily routines through interactive checklists.

## What does it do?

- Displays current date and time
- Interactive morning routine checklist with medication reminders
- Pet care checklist for multiple animals
- Evening routine with conditional logic (optional items based on user input)
- Dynamic checkmarks based on your responses

## Why this project?

This is my first Python project, built as part of my learning path toward becoming a SOC Analyst via [OptiSec](https://optisec.nl). Python is an essential skill in cybersecurity — from log parsing and SIEM automation to scripting incident response workflows. Starting with a practical, everyday tool helped me learn core concepts like:

- **User input handling** — validating and responding to `input()`
- **Conditional logic** — `if/else` branching based on user responses
- **Date/time operations** — working with `datetime` for time-aware features
- **String formatting** — clean terminal output with dynamic content
- **Program flow** — structuring a multi-step interactive application

## How to use

1. Make sure Python 3 is installed
2. Clone the repository:
   ```bash
   git clone https://github.com/MFABrouwer/Daily-schedule-tracker.git
   cd Daily-schedule-tracker
   ```
3. Run in your terminal:
   ```bash
   python checklist.py
   ```

## Requirements

- Python 3.6+
- No external dependencies (uses only the standard library)

See [requirements.txt](requirements.txt) for details.

## What's next?

As I progress through my SOC Analyst training, I plan to expand this project and build new tools:

- **Logging**: Write completed checklists to a log file (practice for log analysis)
- **JSON config**: Load checklist items from a config file instead of hardcoding
- **Argparse**: Add command-line arguments (e.g. `--morning`, `--evening`)
- **Security automation scripts**: New repo with tools for log parsing, hash verification, and more

## About the author

I'm Marc Brouwer — an IT professional transitioning into cybersecurity. With 20+ years of hands-on tech experience and a strong analytical profile, I'm building my skills one project at a time.

- 🌐 [Portfolio](https://mfabrouwer.github.io/Hello-World/)
- 💼 [GitHub](https://github.com/MFABrouwer)

## License

This project is open source and available for learning purposes.
