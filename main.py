from converter import convert_python_to_js

def main():
    print("🔄 Python to JavaScript Converter")
    python_code = """
def greet(name):
    print(f'Hello, {name}!')

greet('John')
"""
    js_code = convert_python_to_js(python_code)
    print("\n🔹 Converted JavaScript Code:\n")
    print(js_code)

if __name__ == "__main__":
    main()
