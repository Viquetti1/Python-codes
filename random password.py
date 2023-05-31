import random as rd

#This code generate a random password, the user need to input the number of letters, symbols and numbers to work!

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for letter in range(nr_letters,0,-1):
    password += rd.choice(letters)

for symbol in range(nr_symbols,0,-1):
    password += rd.choice(symbols)
    

for number in range(nr_numbers,0,-1):
    password += rd.choice(numbers)

#embaralhar a complete_password 
rd.shuffle(password)
print(password)

#loop for para concatenar os digitos da lista
complete_password = " "
for letra in(password):
    complete_password += letra

print(complete_password)
    
    



    













