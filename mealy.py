
# Initialization of the Mealy machine
# print(“comma separated ip”)

ns = set(input("Enter the states: ").split(","))
ni = set(input("Enter the inputs: ").split(","))
q = input("Enter the start state: ")

transitions = {}

for state in ns:
    transitions[state] = {}
    for inp in ni:
        next_state = input(f"Enter next state for {state} on input {inp}: ")
        output = input(f"Enter output for {state} on input {inp}: ")
        transitions[state][inp] = (next_state, output)

# Main loop for validating strings
while True:
    ip = input("Enter the string to process: ")
    path = [q]
    output_path = ""

    for i in range(len(ip)):
        next_state, output = transitions[path[i]][ip[i]]
        path.append(next_state)
        output_path += output

    print("Path:")
    for i in range(len(ip)):
        print(f"{path[i]}-{ip[i]}-->", end=" ")

    print("\nOutput sequence:", output_path)



    choice = input("Do you want to validate another string? (y/n): ")
    if choice.lower() == "n":
        break

