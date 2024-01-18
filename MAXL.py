l1 = []
max_num = 0
size = int(input('How many elements you want to enter? '))
print('Enter',str(size),'positive numbers:')
for i in range(size):
    elements = int(input(""))
    l1.append(elements)
for elements in l1:
    if elements > max_num:
        max_num = elements

print('The largest number in list is:', max_num)