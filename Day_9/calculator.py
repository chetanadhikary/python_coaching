def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x,y

def div(x,y):
    return x/y

if __name__ == '__main__':
    x1 = float(input('Input first number'))
    x2 = float(input('Input second number'))

    choice = int(input('Choose the operation\n1->Addition\n2->Subtraction\n3->Multiplication\n4->Division'))

    if choice==1:
        result= add(x1,x2)
        print(f'result: {result}')
    elif choice==2:
        result= sub(x1,x2)
        print(f'result: {result}')
    elif choice==3:
        result= mul(x1,x2)
        print(f'result: {result}')
    elif choice==4:
        result= div(x1,x2)
        print(f'result: {result}')
