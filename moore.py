# Initialization of the MOORE machine
ns = set(input("Enter the states: ").split(","))
ni = set(input("Enter the inputs: ").split(","))
q = input("Enter the start state: ")

transitions = {}
outputs={}

for state in ns:
    transitions[state] = {}
    for inp in ni:
        next_state = input(f"Enter next state for {state} on input {inp}: ")
        transitions[state][inp] =next_state

for state in ns:
    outputs[state]=input(f" enter output for state {state} :")
# Main loop for validating strings
while True:
    ip = input("Enter the string to process: ")
    path = [q]
    output_path =outputs[q]

    for i in range(len(ip)):
        next_state= transitions[path[i]][ip[i]]
        path.append(next_state)
        output_path +=outputs[next_state]

    print("Path:")
    for i in range(len(ip)):
        print(f"{path[i]}-{ip[i]}-->", end=" ")

    print("\nOutput sequence:", output_path)


    choice = input("Do you want to validate another string? (y/n): ")
    if choice.lower() == "n":
        break
