

def calculate(function,  numb1):



    if function=="+":
       
        num2=int(input("What is your second number? "))
        output=numb1+num2
    elif function=="-":
        
        number2=int(input("What is your second number? "))
        output=numb1-number2

    elif function=="*":
        
        numb2=int(input("What is your second number? "))
        output=numb1*numb2
    elif function=="/":
        
        numb2=int(input("What is your second number? "))
        output=numb1/numb2

    elif function=="^2":
        
        output=numb1**2

    elif function=="^X":
       
        numb2=int(input("What is your second number? "))
        output=numb1**numb2
    elif function=="sqrt":
    
        output=numb1**0.5

    return output


num1 = int(input("What is your first number? "))
while True:
    f=input("What is your function? + , - , * , / , ^2, ^X, sqrt ")
    
    output=calculate(f, num1)
    num1=output
    print(output)
    