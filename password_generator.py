import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# easy version of the generator
# list to store all of user's random characters
selected_characters = ""

for i in range(0, nr_letters):
    selected_characters += random.choice(letters)
    
for i in range(0, nr_symbols):
    selected_characters += random.choice(symbols)
    
for i in range(0, nr_numbers):
    selected_characters += random.choice(numbers)
    
print("Your password is (easy version):",selected_characters)

# hard version continuation
selected_characters = []

for i in range(0, nr_letters):
    selected_characters.append(random.choice(letters))
    
for i in range(0, nr_symbols):
    selected_characters.append(random.choice(symbols))
    
for i in range(0, nr_numbers):
    selected_characters.append(random.choice(numbers))
    
print(selected_characters)
random.shuffle(selected_characters) # shuffle can only be done in place not assigned to variable
print(selected_characters)

password = ""
for char in selected_characters:
    password += char
print("Your password is:", password)

# Alternative way of joining characters from list to a string
# print("Your password is:", "".join(selected_characters))
