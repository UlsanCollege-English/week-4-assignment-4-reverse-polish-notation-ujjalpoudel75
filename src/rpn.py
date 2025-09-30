# /src/rpn.py

def eval_rpn(tokens):
    """
    Evaluates a Reverse Polish Notation (RPN) expression given as a list of tokens.
    Performs integer division that truncates toward zero (as required by tests).
    """
    stack = []
    
    # Set of supported operators
    operators = {'+', '-', '*', '/'}

    for token in tokens:
        if token not in operators:
            # Token is a number: push its integer value onto the stack.
            stack.append(int(token))
        else:
            # Token is an operator: pop two operands (b then a).
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                # Use int(a / b) to achieve truncation toward zero (floor for positive, ceil for negative).
                result = int(a / b) 
            
            # Push the result back onto the stack
            stack.append(result)

    # The final result is the only remaining item on the stack
    return stack[0]