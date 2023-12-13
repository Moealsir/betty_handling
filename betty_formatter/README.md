# Betty Formatter

Betty Formatter is a tool that helps you automatically fix and format your C source code according to the Betty coding style.

## Features

- **Error Capture:** Capture and display Betty-style errors for each file.
- **Whitespace Formatting:** Replace spaces with tabs, add parentheses around return values, and add spaces after commas.
- **Comment Handling:** Remove single-line comments found alone in a line or after a code line.
- **Consecutive Blank Line Removal:** Remove multiple consecutive blank lines.
- **Whitespace Trailing Removal:** Remove trailing whitespaces at the end of lines.
- **Consistent Line Endings:** Add a line without a newline at the end of each file.

### Requirements

Make sure you have `betty` installed. You can download Betty from [here](https://github.com/holbertonschool/Betty).

### Installation

Clone the repository:

```bash
git clone https://github.com/Moealsir/betty_handling.git
```
Copy script to Home
```bash
cp betty_formatter.py ~/.betty_formatter.py
```

### Usage

Run the Betty Formatter on your C files:
```bash
python3 ~/.betty_formatter.py file1.c file2.c ...
```
This will display errors, fix the style issues, and update the files in-place.
