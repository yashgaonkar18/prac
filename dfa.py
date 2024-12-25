def transition(state, symbol):
    if state == 0 and symbol == '0':
        return 0
    elif state == 0 and symbol == '1':
        return 1
    elif state == 1 and symbol == '0':
        return 1
    elif state == 1 and symbol == '1':
        return 2
    elif state == 2 and symbol == '0':
        return 2
    else:
        return -1  # Invalid state


def is_accepted(input_string):
    current_state = 0  # Start state

    for symbol in input_string:
        current_state = transition(current_state, symbol)
        if current_state == -1:  # Invalid state
            return False

    return current_state == 2  # Accepting state


input_string = input("Enter a string: ")
if is_accepted(input_string):
    print("Accepted")
else:
    print("Not Accepted")