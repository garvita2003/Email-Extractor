# Email-Extractor 📧

## 📌 Introduction

**Email-Extractor** is a Python utility tool that extracts email addresses from given text using regular expression pattern matching. This project demonstrates the power of regex in Python and the `re` module's `findall()` function to identify and extract valid email addresses from unstructured text data.

**Key Features:**
- ✅ Extract multiple email addresses from text
- ✅ Pattern-based email validation
- ✅ Support for standard email formats
- ✅ Simple command-line interface
- ✅ Efficient text processing
- ✅ Case-insensitive email extraction

---

## 🔄 Process / Flow

**Key Steps:**
1. User provides a paragraph or block of text containing email addresses
2. The application reads the input text from user input
3. Regular expression pattern matches valid email formats
4. `re.findall()` function finds all email matches in the text
5. All extracted emails are collected in a list
6. Extracted emails are displayed to the user as output

**Email Pattern Matching:**
- Pattern: `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b`
- Validates: alphanumeric characters, dots, underscores, percent signs, plus signs, hyphens
- Local part: before the @ symbol
- Domain name: after the @ symbol
- Top-level domain: minimum 2 letters after the final dot

---

## 🛠️ Technology Used

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3 |
| **Pattern Matching** | Regular Expressions (re module) |
| **Key Function** | re.findall() |
| **Input/Output** | Command-line interface |

**Language Composition:**
- Python: 100%

**Core Modules:**
- `re` - Regular expression module for pattern matching

---

## 🎓 Skills Gained

**Python Programming:**
- ✅ Regular expression (regex) pattern matching
- ✅ String manipulation and processing
- ✅ Function definition and implementation
- ✅ Input/output handling
- ✅ List data structures

**Regular Expressions:**
- ✅ Character classes and quantifiers
- ✅ Pattern boundaries and anchors
- ✅ Email format validation
- ✅ re.findall() function usage
- ✅ Regex pattern construction and optimization

**Programming Concepts:**
- ✅ Function-based modular code
- ✅ Error-free pattern matching
- ✅ Data collection and processing
- ✅ Text parsing and extraction

---

## 📂 Project Structure

```
Email-Extractor/
├── EmailExtract/                # Main project directory
│   └── code.py                  # Main Python script with email extraction logic
├── README.md                    # Project documentation
└── .gitignore                   # Git ignore file
```

---

## 📸 Demonstration

**Sample Output:**
![Screenshot 2024-09-09 100743](https://github.com/user-attachments/assets/6aa876bd-cc09-409d-8325-e276eda75c8c)

---

## ⚙️ Setup Instructions

### Prerequisites:
- Python 3.x installed on your system
- Terminal/Command Prompt access
- Text editor or IDE (optional)

### Installation Steps:

```bash
# 1. Clone the repository
git clone https://github.com/garvita2003/Email-Extractor.git
cd Email-Extractor

# 2. Navigate to the project directory
cd EmailExtract

# 3. Run the Python script
python code.py
```

---

## 📋 How to Use

1. **Run the Program:**
   ```bash
   python code.py
   ```

2. **Provide Input:**
   - When prompted, enter a paragraph or text containing email addresses
   - Example input:
     ```
     Contact us at support@example.com or sales@company.org for more information. 
     You can also reach john.doe@email.co.uk or mary_smith@test.net
     ```

3. **View Output:**
   - The program will display all extracted email addresses:
     ```
     Extracted emails : ['support@example.com', 'sales@company.org', 'john.doe@email.co.uk', 'mary_smith@test.net']
     ```

---

## 🔍 Regular Expression Pattern Explained

**Pattern:** `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b`

**Breakdown:**
- `\b` - Word boundary (start)
- `[A-Za-z0-9._%+-]+` - Local part (username): allows letters, numbers, dots, underscores, percent, plus, hyphen
- `@` - Literal @ symbol
- `[A-Za-z0-9.-]+` - Domain name: allows letters, numbers, dots, hyphens
- `\.` - Literal dot before TLD
- `[A-Z|a-z]{2,}` - Top-level domain: at least 2 letters (case-insensitive)
- `\b` - Word boundary (end)

---

## ✅ Supported Email Formats

The script supports the following email formats:
- `user@example.com` - Standard format
- `first.last@example.com` - Dot in local part
- `user+tag@example.com` - Plus sign for email filtering
- `user_name@example.co.uk` - Underscore and multiple domain levels
- `user123@domain456.org` - Numbers in both parts
- `john-doe@company.net` - Hyphen in domain or local part

---

## ⚠️ Limitations

- Does not validate if the email actually exists
- Does not check email server validity
- Does not support internationalized domain names (IDN)
- Does not validate subdomain depth
- Requires plain text input (works best with text, not HTML)

---

## 🚀 Possible Enhancements

```python
# Potential improvements:
# 1. File input - read from text files
# 2. Email validation - verify email existence
# 3. Duplicate removal - filter duplicate emails
# 4. Export functionality - save results to CSV/JSON
# 5. GUI interface - create a graphical user interface
# 6. Email filtering - filter by domain or criteria
```

---

## 📝 Example Usage

```python
# Run the script
$ python code.py

# Enter a paragraph of text containing email ids : 
# Hello! Please contact john@example.com or support@mycompany.org for assistance.

# Output:
# Extracted emails : ['john@example.com', 'support@mycompany.org']
```

---

## 💡 Learning Resources

This project teaches:
- How to use Python's `re` module effectively
- Regular expression pattern construction
- Text processing and string manipulation
- Function-based code organization
- User input/output handling in Python
