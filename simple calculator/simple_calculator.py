def addition(n1,n2):
    total = n1 + n2
    return  total
def multiply(n1,n2):
    total = n1 * n2
    return  total
def subtract(n1,n2):
    total = n1 - n2
    return  total
operation_deck = {
    '+' : addition,
    '*' : multiply,
    '-' : subtract,
}



def calculator():
    print('CALCULATOR APP')
    first_number = int(input('Enter a number: '))
    calc_over = False
    while not calc_over:

        for keys in operation_deck:

            print(keys)
        enter_opera = input('Enter provided operation: ')
        second_number = int(input('Enter second number: '))
        answer = operation_deck[enter_opera](first_number, second_number)
        print(answer)
        continue_game = input(f'Do u want to continue with answer as {answer} y or n?: ').lower()
        if continue_game == 'y':
            first_number = answer

        else:
            calc_over = True
            calculator()
calculator()
