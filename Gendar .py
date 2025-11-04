def prefix(name,gender):
   if gender=='M'or gender=='m':
       print(f"Hello,Mr.",name)
   elif gender=='F' or gender=='f':
       print("Hello,Ms.",name)
   else:
       print("pleas enter only M andF for gender")
name=input("enter your name")
gender=input("enter your gender: M for male ,F for female")                
prefix(name,gender) 