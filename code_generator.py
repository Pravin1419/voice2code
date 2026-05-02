import re

# 🔧 Clean speech text
def clean_text(text):
    text = text.lower()

    # Convert time format like 1:00 → 1
    text = re.sub(r'(\d+):\d+', r'\1', text)

    # Normalize words
    text = text.replace("-", " ").replace("to", " ")

    return text


# 🔧 Extract numbers safely
def extract_range(text):
    text = clean_text(text)

    numbers = list(map(int, re.findall(r'\d+', text)))

    if len(numbers) >= 2:
        return numbers[0], numbers[1]

    return None, None


# 🚀 Main generator
def generate_code(text):
    text = text.lower()

    # 1. Hello World
    if "hello world" in text:
        return 'print("Hello World")'

    # 2. Print numbers loop
    elif "print numbers" in text or "numbers" in text:
        start, end = extract_range(text)

        if start is not None:
            if start <= end:
                return f"""for i in range({start}, {end+1}):
    print(i)"""
            else:
                return f"""for i in range({start}, {end-1}, -1):
    print(i)"""

    # 3. Take input
    elif "take input" in text:
        return """x = input("Enter value: ")
print(x)"""

    # 4. Fallback
    return "# Command not recognized"