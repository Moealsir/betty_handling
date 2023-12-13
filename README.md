# Betty Scripts

Betty Scripts is a collection of utility tools designed to assist in organizing and formatting C source code files to meet specific coding standards.

## Features

### Betty Handler

- **Tasks Directory Creation:** Automatically creates a 'tasks' directory to organize and store modified files.
- **File Copying:** Copies specified C files to the 'tasks' directory, excluding lines starting with `#include` that end with '.h".
- **Main File Modification:** Modifies main C files to include only the necessary '#include' lines from the 'tasks' directory.

### Betty Formatter

- **Error Capture:** Capture and display Betty-style errors for each file.
- **Whitespace Formatting:** Replace spaces with tabs, add parentheses around return values, and add spaces after commas.
- **Comment Handling:** Remove single-line comments found alone in a line or after a code line.
- **Consecutive Blank Line Removal:** Remove multiple consecutive blank lines.
- **Whitespace Trailing Removal:** Remove trailing whitespaces at the end of lines.
- **Consistent Line Endings:** Add a line without a newline at the end of each file.

### Requirements

Ensure you have Python installed on your system.

### Read README.md files for more informations
