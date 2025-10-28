from datetime import datetime 

def welcome_message():
    print(" Welcome to our website!")
    print("We’re glad to have you here. pleas enter the valuable deatles!")
    
welcome_message()

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

name=input("enter your name:")

while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Invalid age! Enter a valid number.")

valid_gender = ["male", "female", "other", "m", "f", "o"]

while True:
     sex = input("Enter your gender (Male/Female/Other): ").lower()
     if sex in valid_gender:
         break
     else:
        print("Invalid! Please enter Male, Female, or Other.")
            
address=input("enter your full address:")

while True:
        phone = input("Enter your phone number (10 digits only): ")
        if phone.isdigit() and len(phone) == 10:
            break
        else:
            print("Invalid! Phone number must contain exactly 10 digits.")

while True:
        email = input("Enter your email: ")
        if "@" in email and "." in email:
            break
        else:
            print("Invalid email format! Example: abc@gmail.com")

print("\n----- USER DETAILS -----")
print("date and time:",current_time)
print("name:",name)
print("age:",age)
print("gender:",sex.capitalize())
print("address:",address)
print("phone:",phone)
print("email:",email)

if age>=18:
    print(f"Dr {name},you are meture enouch to vote the candiate in election commission")
else:
    print(f"we are sorry {name},you are not meture enough to vote the candiate in election commission ")