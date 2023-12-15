def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    print (logo)    
    num1 = float(input("Enter the first number: "))
    
    for items in operations:
        print(items)
    should_continue = True
    while should_continue:
        
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Enter the next number: "))
        calc_function = operations[operation_symbol]
        answer = calc_function(num1,num2)
        print (f"{num1} {operation_symbol} {num2} = {answer}")
        
        next_question = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculator.: ")
        if next_question == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
            

calculator()
