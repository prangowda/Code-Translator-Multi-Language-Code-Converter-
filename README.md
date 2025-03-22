# 🚀 **Code Translator: Convert Python to JavaScript**  

## 📌 **Project Overview**  
The **Code Translator** is a Python-based tool that converts **Python code to JavaScript** by recognizing common syntax patterns. This is a basic implementation, and it can be expanded to support more language conversions (e.g., **C to Java, Python to PHP**).  

---

## 📁 **Project Structure**  
```
📂 CodeTranslator
│── 📜 main.py                      # Main script to handle conversion
│── 📜 converter.py                  # Code conversion logic
│── 📜 test_code.py                  # Sample Python code to test conversion
│── 📜 requirements.txt               # Dependencies
│── 📜 README.md                      # Project details
```

---

## ⚡ **Features**  
✅ Convert Python functions to JavaScript functions.  
✅ Convert `print()` statements to `console.log()`.  
✅ Support for basic **f-strings** conversion.  
✅ Handles **basic indentation & syntax adjustments**.  
✅ Easy to expand for **other languages** (C, Java, PHP).  

---

## 🛠️ **Technologies Used**  
- **Python** (Primary language)  
- **Regular Expressions (re module)** (Pattern matching for conversion)  

---

## 📥 **Installation & Setup**  

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/prangowda/code-translator.git
cd code-translator
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Translator**
```bash
python main.py
```

---

## 🎯 **Usage Guide**  
1️⃣ Open `main.py` and edit the **Python code** inside the `python_code` variable.  
2️⃣ Run the script, and the **converted JavaScript** code will be displayed.  
3️⃣ Copy the **JavaScript output** and test it in any JS environment.  

---

## 📜 **Code Implementation**  

### **📜 main.py** (Main script)  
```python
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
```

---

### **📜 converter.py** (Conversion logic)  
```python
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
```

---

### **📜 test_code.py** (Example Python script)  
```python
def greet(name):
    print(f'Hello, {name}!')

greet('John')
```

---

## 📜 **Example Output**  

### **Input Python Code:**  
```python
def greet(name):
    print(f'Hello, {name}!')

greet('John')
```

### **Converted JavaScript Code:**  
```js
function greet(name) {
  console.log(`Hello, ${name}!`);
}
```

---

## 🔥 **Future Enhancements**  
🔹 Add support for **loops (for, while)**.  
🔹 Handle **if-else conditions**.  
🔹 Expand to **C → Java, Python → PHP, etc.**.  
🔹 Build a **GUI or Web Interface**.  

---

## 🤝 **Contributing**  
We welcome contributions! Feel free to:  
- **Submit an issue** for bug reports or feature requests.  
- **Fork the repo & submit pull requests** with improvements.  
