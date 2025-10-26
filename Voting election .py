def welcome_message():
    print(" Welcome to our website!")
    print("We’re glad to have you here. pleas enter the valuable deatles!")
    
welcome_message()
    
name=input("enter your name:")
age=int(input("enter your age:"))
sex=input("enter your gender:")
address=input("enter your full address:")
phone=input("enter your phone number:")

print("\n----- USER DETAILS -----")
print("name:",name)
print("age:",age)
print("gender:",sex)
print("address:",address)
print("phone:",phone)

if age>=18:
    print(f"Dr {name},you are meture enouch to vote the candiate in election commission")
else:
    print(f"we are sorry {name},you are not meture enough to vote the candiate in election commission ")
    

