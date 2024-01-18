str1=input("ENTER A STRING:")
str2=input("ENTER A STRING:")
l1=list(set(str1)&set(str2))
print("The common letters are:")
for i in l1:
    print(i)