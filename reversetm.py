
transitions = {
    0: {"a": (0, "a", 1), "b": (0, "b", 1), " ": (1, " ", 0)},  # Move to end
    1: {"a": (2, "_", 0), "b": (3, "_", 0), " ": (4, " ", 1)},  # Replace and go left
    2: {"a": (2, "a", 0), "b": (2, "b", 0), " ": (0, "a", 1)},  # Place 'a' back
    3: {"a": (3, "a", 0), "b": (3, "b", 0), " ": (0, "b", 1)},  # Place 'b' back
    4: {"a": (4, "a", 1), "b": (4, "b", 1), " ": (4, " ", 1)},  # Finished state
}

def turing_machine(input_string):
    # Initialize tape
    tape = list(input_string) + [" "]
    head = 0
    state = 0

    print("Initial Tape:", "".join(tape))
    print(f"Initial State: {state}, Head: {head}")

    while state != 4:  # Stop when in the accept state (4)
        # Expand tape if head moves out of bounds
        if head < 0:
            tape.insert(0, " ")
            head = 0
        elif head >= len(tape):
            tape.append(" ")

        current_symbol = tape[head]

        if current_symbol not in transitions[state]:
            print("Error: Unexpected symbol!")
            break

        next_state, replace_symbol, direction = transitions[state][current_symbol]

        # Update tape and move head
        tape[head] = replace_symbol
        state = next_state
        head += 1 if direction == 1 else -1

        print("Tape:", "".join(tape))
        print(f"State: {state}, Head: {head}")

    # Remove trailing spaces
    reversed_string = "".join(tape).strip()
    return reversed_string

# Input from the user
input_string = input("Enter the string to reverse (using 'a', 'b'): ")
result = turing_machine(input_string)
print("Reversed String:", result)