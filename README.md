# University Assignments

My coursework from King Saud University (KSU), organized by course. Each lab or
assignment lives in its own folder.

## Structure

```
IS-324-python/
├── lab1/lab1.py
├── lab2/lab2.py
└── lab3/lab3.py
```

| Course | Language | Contents |
|---|---|---|
| IS 324 | Python | Labs 1 to 3 |

More courses will get their own top-level folder as I add them.

## Running a lab

Python 3 is required. From the repo root:

```bash
python3 IS-324-python/lab3/lab3.py
```

Labs 1 and 2 define a `program1()`, `program2()`, ... function for each question,
so import the file (or call the functions from a Python shell) to run a specific
program.

## Workflow

- `main` holds finished work.
- Each lab is developed on its own branch (for example `is324/lab3`), opened as a
  pull request, and merged into `main`.
