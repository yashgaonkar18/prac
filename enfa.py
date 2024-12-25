#enfa(a+b)*.a
def transition(state, symbol):
    if state == 0 and symbol == 'a':
        return {0, 1}
    elif state == 0 and symbol == 'b':
        return {0}
    elif state == 1 and symbol == 'a':
        return {1}
    elif state == 1 and symbol == 'b':
        return {1}
    else:
        return set()


def is_accepted(input_string):
    current_states = {0}

    for symbol in input_string:
        next_states = set()
        for state in current_states:
            next_states |= transition(state, symbol)
        current_states = next_states

    return 1 in current_states

input_string = input("Enter a string: ")
if is_accepted(input_string):
    print("Accepted")
else:
    print("Not Accepted")