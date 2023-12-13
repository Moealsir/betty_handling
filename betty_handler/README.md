# Betty Handler

Betty Handler is a utility tool that assists in organizing and modifying C source code files to meet specific requirements.

## Features

- **Tasks Directory Creation:** Automatically creates a 'tasks' directory to organize and store modified files.
- **File Copying:** Copies specified C files to the 'tasks' directory, excluding lines starting with `#include` that end with '.h"'
- **Main File Modification:** Modifies main C files to include only the necessary '#include' lines from the 'tasks' directory.

### Requirements

Ensure you have Python installed on your system.

### Installation

Clone the repository:

```bash
git clone https://github.com/Moealsir/betty_handling.git
```
Navigate to the project directory:
```bash
cd betty-handler
```
Copy script to Home
```bash
cp betty_handler.py ~/.betty_handler.py
```
Run the Betty Handler on your C files:
```bash

### Usage

python betty_handler.py file1.c file2.c ...
```
This will create a 'tasks' directory, copy specified files, and modify the main files to include only necessary '#include' lines.
