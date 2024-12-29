def nfa_to_dfa(nfa, start_state, final_states):
    dfa, queue, processed, dfa_final_states = {}, [frozenset([start_state])], set(), set()

    while queue:
        current = queue.pop(0)
        if current in processed:
            continue
        processed.add(current)
        dfa[current] = {}

        for symbol in nfa['symbols']:
            reachable = frozenset(state for s in current if s in nfa['transitions'] and symbol in nfa['transitions'][s] for state in nfa['transitions'][s][symbol])
            if reachable:
                dfa[current][symbol] = reachable
                if reachable not in processed:
                    queue.append(reachable)

        if current & final_states:
            dfa_final_states.add(current)
    return dfa, dfa_final_states


nfa = {
    'states': {'q0', 'q1', 'q2'},
    'symbols': {'a', 'b'},
    'transitions': {
        'q0': {'a': {'q0', 'q1'}, 'b': {'q0'}},
        'q1': {'b': {'q2'}},
        'q2': {}
    }
}

start_state, final_states = 'q0', {'q2'}
dfa, dfa_final_states = nfa_to_dfa(nfa, start_state, final_states)

print("DFA Transitions:")
for state, transitions in dfa.items():
    print(f"State {','.join(state)}:")
    for symbol, target in transitions.items():
        print(f"  On '{symbol}' -> {','.join(target)}")

print("\nDFA Final States:")
for state in dfa_final_states:
    print(','.join(state))
