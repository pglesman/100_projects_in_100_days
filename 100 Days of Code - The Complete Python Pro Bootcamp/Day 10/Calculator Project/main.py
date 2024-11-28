import art

print(art.logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


dictionary = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide,
              }

while True:
    first_number = int(input("Write the first number: "))
    while True:
        for key in dictionary:
            print(key)

        operation = input("Chose a given above mathematical operation: ")
        second_number = int(input("Write the second number: "))
        result = dictionary[operation](first_number, second_number)

        print(f'{first_number} {operation} {second_number} = {result}')

        calc_next = input("Do you want to continue working with previous result? Yes or no?").lower()
        if calc_next == 'no':
            break

        first_number = result
