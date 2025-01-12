# Ask user for their name + remove whitespace from str and capitalize
name = input("What's your name? ").strip().title()

#  split the firstname and lastname
fname, lname = name.split(" ")

# Say hello to user
print(f"Hello, {fname} {lname}")