def convert(string):
  newstring=string.title()
  print("the input string in title case:",newstring)
userinput=input("enter a sentence")
totalspace=0
for b in userinput:
    if b.isspace():
        totalspace+=1
if(userinput.istitle()):
     print("the string is already in tutle case")
elif(totalspace>0):
     convert(userinput)
else:
     print("the string has only one word")
        