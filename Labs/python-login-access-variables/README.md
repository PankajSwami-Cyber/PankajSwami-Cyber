# Python Login Access Variables

A beginner Python practice project based on a security-analyst scenario. It demonstrates how to store login-related information in variables, inspect data types, update an allow-list, and compare login attempts against a limit.

> **Learning exercise only:** this project does not authenticate users, enforce account lockouts, or secure a real device. Do not use it as production access-control software. The usernames are example data from the exercise; never publish real employee or customer identifiers.

## Learning objectives

- Assign values to variables.
- Work with strings, lists, integers, and Booleans.
- Use `type()` to inspect a variable's data type.
- Reassign a list when approved usernames change.
- Use `<=` to compare current login attempts with a configured maximum.

## Project files

```text
python-login-access-variables/
├── README.md
├── login_access_variables.ipynb
├── login_access_variables.py
└── .gitignore
```

## Run the project

### Option 1: Run the Python script

Python 3 is required. No third-party packages are needed.

```bash
python login_access_variables.py
```

### Option 2: Run the notebook

Open `login_access_variables.ipynb` in Jupyter Notebook, JupyterLab, or Google Colab. Run the cells from top to bottom.

## Expected concepts and results

| Variable | Example value | Python data type |
|---|---|---|
| `device_id` | `"72e08x0"` | `str` |
| `username_list` | List of approved usernames | `list` |
| `max_logins` | `3` | `int` |
| `login_attempts` | `2` | `int` |
| `login_status` | `False` | `bool` |

With `login_attempts = 2` and `max_logins = 3`, the expression `login_attempts <= max_logins` evaluates to `True`. With `login_attempts = 4`, it evaluates to `False`.

## Key takeaways

Python variables make it easier to organize information used in security-related programs. Data types determine the kind of value a variable stores, while comparison operators produce Boolean results that can be used by later decision-making logic.

## Possible next improvements

- Check whether a username exists in `username_list`.
- Write a function that reports whether the login-attempt limit has been reached.
- Add input validation so negative attempt counts are rejected.
- Write unit tests for the comparison logic.

## Attribution and sharing note

This is a personal learning/portfolio adaptation of a beginner lab scenario. Add the name of the course or learning provider if required by its sharing rules. Do not upload proprietary course instructions, answer keys, or screenshots unless the provider permits redistribution.
