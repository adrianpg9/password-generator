#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

#the following line ask the user how many of each character type they want in their password 
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password = [] # empty list to store the chracters 

#following lines generate random characters for the password based on the parameters set by the user
final_password = ""
for char in range(1, nr_symbols + 1):
  password.append(random.choice(symbols))

for char in range(1, nr_letters + 1):
  password.append(random.choice(letters))

for char in range(1, nr_numbers + 1):
  password.append(random.choice(numbers)) 


for current_password in range(0, len(password)):
 
  current_char = str(random.choice(password)) #obtains a random element for the list 


  final_password += current_char #appeands the randomly selecet element of the list to the final password 
  password.remove(current_char) # removes the element so it cannot be used again 

  
print("Hard Password: " + str(final_password)) # prints the finalize password 


