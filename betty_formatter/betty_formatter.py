import re
import sys
import subprocess

def capture_and_display_betty_errors(file_paths):
    # Capture Betty-style errors for each file and display them
    for file_path in file_paths:
        result = subprocess.run(['betty', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        errors = re.findall(r'(\d+-[^:]+:\d+: [^\n]+)', result.stderr)
        if errors:
            print(f"Errors in {file_path}:")
            for error in errors:
                print(error)

def fix_main_declaration(content):
    # Fix main declaration: int main() should be int main(void)
    return re.sub(r'\b(int\s+main\s*\(\s*\))', r'int main(void)', content)
    
def fix_space_before_open_parenthesis(content):
    # Fix space between function name and open parenthesis
    return re.sub(r'(\b\w+\s+)\(', r'\1(', content)

def fix_brace_placement_conditions(content):
    # Add a new feature: open braces '{' following conditions go on the next line
    keywords = r'\b(?:if|else|while|for|switch|do|else if|case|default|try|catch|finally|return)\b'
    content = re.sub(rf'({keywords}\s*\(.*\))\s*{{', r'\1\n{', content)

    # Handle "else {" case
    content = re.sub(r'else\s*{', 'else\n{', content)

    # Handle "} else {" case
    content = re.sub(r'}\s*else\s*{', '}\nelse\n{', content)

    return content

def fix_brace_placement(content):
    # Add a new feature: open braces '{' following function declarations go on the next line
    function_keywords = r'\b(?:int|void|char|float|double|long|unsigned|signed|static|const|inline)\b'
    return re.sub(rf'({function_keywords}\s+\w+\s*\(.*\))\s*{{', r'\1\n{', content)

def replace_spaces_with_tabs(content):
    # Replace spaces with tabs in the leading whitespace of lines
    return re.sub(r'^[ ]+', lambda x: '\t' * (len(x.group(0)) // 8), content, flags=re.MULTILINE)

def add_parentheses_around_return(content):
    # Add parentheses around return values if not already present
    content = re.sub(r'return[ ]+([^(][^;]+);', r'return (\1);', content)
    
    # Add parentheses around return values if no value is present and not already in parentheses
    return re.sub(r'return[ ]+([^;()]+);', r'return (\1);', content)

def add_space_after_comma(content):
    # Add space after ',' character
    return re.sub(r',(?![ \t])', r', ', content)

def remove_single_line_comments(content):
    # Remove single-line comments (//) found alone in a line or after a code line
    return re.sub(r'([^;])\s*//.*|^\s*//.*', r'\1', content, flags=re.MULTILINE)

def remove_consecutive_blank_lines(content):
    # Remove multiple consecutive blank lines
    return re.sub('\n{3,}', '\n\n', content)

def remove_trailing_whitespaces(content):
    # Remove trailing whitespaces at the end of lines
    return re.sub(r'[ \t]+$', '', content, flags=re.MULTILINE)

def add_line_without_newline(file_path, line):
    # Add a line without a newline at the end of the file if not found
    with open(file_path, 'r') as file:
        lines = file.readlines()
        last_line = lines[-1] if lines else ''

    if not last_line.strip() == line.strip():
        with open(file_path, 'a') as file:
            file.write(line)

def fix_betty_style(file_paths):
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            content = file.read()

        # Apply fixes in a specific order
        content = fix_space_before_open_parenthesis(content)
        content = fix_brace_placement(content)
        content = fix_brace_placement_conditions(content)
        content = fix_main_declaration(content)
        content = remove_single_line_comments(content)
        content = replace_spaces_with_tabs(content)
        content = add_parentheses_around_return(content)
        content = add_space_after_comma(content)
        content = remove_consecutive_blank_lines(content)
        content = remove_trailing_whitespaces(content)

        # Write the fixed content back to the file
        with open(file_path, 'w') as file:
            file.write(content)

        # Add a line without a newline at the end of the file
        add_line_without_newline(file_path, '\n')


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python betty_fixer.py file1.c file2.c ...")
        sys.exit(1)

    file_paths = sys.argv[1:]

    # Capture and display Betty-style errors
    capture_and_display_betty_errors(file_paths)

    # Fix Betty style
    fix_betty_style(file_paths)

    print("Betty style fixed for the following files:", file_paths)

