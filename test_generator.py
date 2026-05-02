from code_generator import generate_code

text = input("Enter your command: ")

code = generate_code(text)

print("\nGenerated Python Code:\n")
print(code)