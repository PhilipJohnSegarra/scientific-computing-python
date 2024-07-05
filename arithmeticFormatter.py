problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]

top_operands = ['4563', '80', '670']
bottom_operands = ['4563', '890', '67']
formatted_top = [' ' * (len(char) + 2 - len(char)) + char for char in top_operands]
formatted_bottom = ['+' + ' ' * (len(char) + 1 - len(char)) + char for char in bottom_operands]

def evaluate(expression):
    operand1 = ''
    operand2 = ''
    maxLength = ''
    result = ''
    
    # Check if the expression is an addition
    if '+' in expression:
        operands = expression.strip().split('+')
        operand1 = operands[0].strip()
        operand2 = operands[1].strip()
        result = int(operand1) + int(operand2)
        maxLength = max(len(operand1), len(operand2))
        return {'operand1': operand1, 'operand2': operand2, 'maxlength': maxLength, 'result': result, 'operand': '+'}
    
    # Check if the expression is a subtraction
    elif '-' in expression:
        operands = expression.strip().split('-')
        operand1 = operands[0].strip()
        operand2 = operands[1].strip()
        result = int(operand1) - int(operand2)
        maxLength = max(len(operand1), len(operand2))
        return {'operand1': operand1, 'operand2': operand2, 'maxlength': maxLength, 'result': result, 'operand': '-'}

def has_letters(problems):
    for item in problems:
        # Remove '+' and '-' characters and update item
        if '+' in item:
            item = item.replace('+', '')
        if '-' in item:
            item = item.replace('-', '')
        item = item.replace(' ', '')
        
        # Check for non-numeric characters in the updated item
        for char in item:
            if not char.isdigit():
                return True  # Found a non-numeric character
    
    return False  # No non-numeric characters found in any item

def invalid_number_of_Digits(problems):
    for item in problems:
        item = item.replace(' ', '')
        nums = []
        
        # Split the item into numbers based on the operator
        if '+' in item:
            nums = item.split('+')
        elif '-' in item:
            nums = item.split('-')
        
        # Check if any number has more than 4 digits
        for num in nums:
            if len(num) > 4:
                return True
    
    return False

def arithmetic_arranger(problems, showResult=False):
    evaluated_problems = []

    # Check if the number of problems exceeds the limit
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # Check if the operator is either '*' or '/'
    if any('*' in element for element in problems) or any('/' in element for element in problems):
        return "Error: Operator must be '+' or '-'."

    # Check if the problems contain any non-numeric characters
    if has_letters(problems) == True:
        return 'Error: Numbers must only contain digits.'

    # Evaluate each problem
    for expression in problems:
        evaluated_problems.append(evaluate(expression))
    
    # Format the top operands
    formatted_top = [' ' * (expression['maxlength'] + 2 - len(expression['operand1'])) + expression['operand1'] for expression in evaluated_problems]
    # Format the bottom operands
    formatted_bottom = [expression['operand'] + ' ' * ((expression['maxlength'] + 1) - len(expression['operand2'])) + expression['operand2'] for expression in evaluated_problems]
    # Format the results
    formatted_result = [' ' * (expression['maxlength'] + 2 - len(str(expression['result']))) + str(expression['result']) for expression in evaluated_problems]
    # Format the dashes
    formatted_bar = [('-' * ((expression['maxlength']) + 2)) for expression in evaluated_problems]

    # Join the formatted strings with spaces
    top_row = '    '.join(formatted_top)
    bottom_row = '    '.join(formatted_bottom)
    bar_row = '    '.join(formatted_bar)
    result_row = ''
    
    # If results need to be shown, add them to the output
    if showResult:
        result_row = '    '.join(formatted_result)
        result_row = f"\n{result_row}"
    
    return top_row + '\n' + bottom_row + '\n' + bar_row + result_row

# Test cases
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

# PROUD TO SAY, WA NIY CHATGPT HAHAHAHHA
