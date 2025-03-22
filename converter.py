import re

def convert_python_to_js(python_code):
    js_code = python_code

    # Convert print statements
    js_code = re.sub(r'print\((.*?)\)', r'console.log(\1);', js_code)

    # Convert function definitions
    js_code = re.sub(r'def (.*?)\((.*?)\):', r'function \1(\2) {', js_code)

    # Convert f-strings (basic handling)
    js_code = re.sub(r'f\'(.*?)\{(.*?)\}(.*?)\'', r'`\1${\2}\3`', js_code)

    # Convert indentation (basic handling)
    js_code = js_code.replace("    ", "  ")

    # Close function brackets
    js_code = re.sub(r'(function .*?)\n', r'\1\n{', js_code)
    js_code += "\n}"  # Close last function

    return js_code
