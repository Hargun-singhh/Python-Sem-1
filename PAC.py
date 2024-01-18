class check():
    def __init__(self):
         self.n = []
    def permeter(self,a):
         per=2*3.14*a
         return per
    def ar(self,a):
        a =3.14*a*a
        return a

obj=check()

print("1.Perimeter of Circle")
print("2.Area Of Circle")
print("3.Exit")
while True:
    choice=int(input("Enter Your choice:"))
    if choice ==1:
        a=float(input("Enter The Radius Of Circle (cm) :"))
        print("Perimeter IS:",obj.permeter(a))
    elif choice==2:
        a = float(input("Enter The Radius Of Circle(cm) :"))
        print("Area Is:",obj.ar(a))
    elif choice==3:
        print("Thanks FOr Using :)")
        exit()

