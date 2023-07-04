# function for checking if input can be parsed to float
def is_float(number) -> bool:
    # if you expect None to be passed:
    if number is None:        
        return None
    try:    
        return float(number)
    except ValueError:
        return None






def calculate_input(number_one, number_two, operator):
    num_one = is_float(number_one)
    num_two = is_float(number_two)
    if num_one == None or num_two == None or operator == None:
        return "Something went wrong with the calculation!"

    if operator == '+':
        answer = num_one + num_two
        return answer
    if operator == '-':
        answer = num_one - num_two
        return answer
    if operator == '/':
        if num_two == 0:
            return "Cannot divide by zero!"
        answer = num_one / num_two
        return answer
    if operator == '*':
        answer = num_one * num_two
        return answer