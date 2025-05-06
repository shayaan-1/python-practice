# Write a function analyze_text(text: str) -> dict that returns a count of:

# Lowercase letters
# Uppercase letters
# Digits
# Special characters (anything else)
# Use a loop and classify each character using built-in string methods.

def scanner(text: str):
    dict = {
        'lowercase': 0,
        'uppercase': 0,
        'digits': 0,
        'special': 0
    }
    for char in text:
        if char.islower():
            dict['lowercase'] += 1
        elif char.isupper():
            dict['uppercase'] += 1
        elif char.isdigit():
            dict['digits'] += 1
        else:
            dict['special'] += 1
    return dict

print(scanner("Hello123!") )