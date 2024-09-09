import re

# Function to implement extraction of email ids
def extract_emails(text):
    # Define a regular expression pattern for matching emails
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Use re.findall to find all matches in the text
    emails = re.findall(email_pattern, text)

    return emails

# Take input text from the user
input_text = input("Enter a paragraph of text containing email ids : ")

# Extract and print the emails from the input text
emails = extract_emails(input_text)
print("Extracted emails :", emails)