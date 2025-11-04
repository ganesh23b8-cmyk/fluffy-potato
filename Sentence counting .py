userinput=input("enter a sentence")
totalchar=len(userinput)
print("total characters:",totalchar)
ta=td=tsp=0
for a in userinput:
    if a.isalpha():
        ta+=1
    elif a.isdigit():
        td+=1
    else:
        tsp+=1
print("total alphabet:",ta)
print("total digit:",td)
print("total special charecter:",tsp)
totalspace=0
for b in userinput :
    if b.isspace():
        totalspace+=0
print("total word in the input:",totalspace+1)