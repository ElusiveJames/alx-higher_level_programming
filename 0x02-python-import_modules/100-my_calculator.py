#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operator = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == '+':
        print(f"{a} {operator} {b} = {calculator_1.add(a,b)}")
    elif operator == '-':
        print(f"{a} {operator} {b} = {calculator_1.sub(a,b)}")
    elif operator == '*':
        print(f"{a} {operator} {b} = {calculator_1.mul(a,b)}")
    elif operator == '/':
        print(f"{a} {operator} {b} = {calculator_1.div(a,b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
