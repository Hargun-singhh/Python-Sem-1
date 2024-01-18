a=str(input("Enter your Name:"))
l1=["a","e","i","o","u","A","E","I","O","U"]
count=0
for i in a:
    if i in l1:
        count +=1
        print("Vowels Are:",i)
print("______RESULT______")
print("Count of Vowels:",count)