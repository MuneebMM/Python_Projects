import random

Letters = ['A','B','C','D','E','F','G','H','I','J'
           ,'K','L','M','N','O','P','Q','R','S','T'
           ,'U','V','W','X','Y','Z']

numbers=['1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')'
           ,'_','+','=']

print("Welcome to my password generator!")
nr_letters = int(input("How many Letters would like to generate in password\n"))
nr_symbols = int(input("How many symbols would you like to generate in the password\n"))
nr_numbers = int(input("How many numbers would you like to generate in the password\n"))

password = []
for char in range(1,nr_letters+1):
   password.append(random.choice(Letters))
for char in range(1,nr_symbols+1):
    password.append(random.choice(symbols))
for char in range(2,nr_numbers+1):
    password.append(random.choice(numbers))

random.shuffle(password)
print("Password is: ", password)

Password = ""
for char in password:
    Password += char

print(f"Your password is: {Password}")