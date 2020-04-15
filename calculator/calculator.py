import re

print("\nMAGIC CALCULATOR")
print("Type quit to exit\n")


previous = 0
run = True

def mathOp():
    global run
    global previous
    equation = ""

    if previous == 0:
        equation = input("Enter your equation: ")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print('Goodbye, CORONA!')
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '',equation)
        
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    mathOp()
