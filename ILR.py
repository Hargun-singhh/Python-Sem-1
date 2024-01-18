l1= input('Enter elements of a list separated by space: \n')
l2 = l1.split()
for i in range(len(l2)):
    l2[i] = int(l2[i])
print("ORIGINAL LIST:\n",l2)
print()
print("REVERSED LIST:\n",l2[::-1])
