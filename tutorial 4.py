
name = (input("What is your name? "))
print("Hello",name,)
A=int(input("What is the value of a?:"))
B=int(input("What is the value of b?: "))
C=int(input("What is the value of c?:"))
D = int(input("What is the value of d?:"))
U = (-B**2 /27*A**3)+(B*C / 6*A**2)-(D / 2*A)
V = (C /3*A)-(B**2 / 9*A**2)
Y = (B/3*A)
sqrROOT = (U**2 + V**3)**(1/2)
cubeROOT1 = (U + sqrROOT)**(1/3)
cubeROOT2 = (U - sqrROOT)**(1/3)
Root = cubeROOT1 + cubeROOT2 -Y
roundedROOT = round(Root.real)
print(roundedROOT)
quit()

