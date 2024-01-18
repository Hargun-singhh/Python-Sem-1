n=int(input("ENTER THE RANGE FOR NATURAL NUMBERS:"))
sum=0
for i in range(1,n+1):
    sum=sum+pow(i,3)
print(">>>RESULT<<<")
print("SUM IS:",sum)