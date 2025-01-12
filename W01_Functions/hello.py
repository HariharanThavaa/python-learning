# Ask user for their name
name = input("What's your name? ")

# Remove whitespace from str
name = name.strip()

# capitalize the name
name = name.title()

# Say hello to user
print(f"Hello, {name}")