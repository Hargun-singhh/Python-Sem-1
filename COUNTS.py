str1 = str(input("ENTER A STRING:"))
dic = {}
for s in str1:
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1
print("_____RESULT_____")
for key in dic:
    print(key, ':', dic[key])
print()
