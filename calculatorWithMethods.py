#-------------Calculator with methods-----------------

def add():
    answer=x+y
    print (answer)
def subtract():
    answer=x-y
    print (answer)
def multiply():
    answer=x*y
    print (answer)
def divide():
    answer=x/y
    print (answer)

x=int(input("What is the first number?"))
y=int(input("What is the second number?"))
oper=input("What operation do you want to do(+,-,*,/)?")

if oper=="+":
    add()
elif oper=="-":
    subtract()
elif oper=="*":
    multiply()
elif oper=="/":
    divide()
else:
    print ("Put the symbol of the operation.")