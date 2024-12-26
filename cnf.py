def cfg_to_cnf(cfg):
    cnf = {}
    counter = 1

    def new_nonterminal():
        nonlocal counter
        nt = f"X{counter}"
        counter += 1
        return nt

    terminal_map = {}

    for nt, productions in cfg.items():
        cnf.setdefault(nt, [])
        for prod in productions:
            if len(prod) > 2:  # Break long productions
                while len(prod) > 2:
                    new_nt = new_nonterminal()
                    cnf[new_nt] = [prod[:2]]
                    prod = new_nt + prod[2:]
                cnf[nt].append(prod)
            elif len(prod) == 1 and prod.islower():  # Single terminal
                if prod not in terminal_map:
                    new_nt = new_nonterminal()
                    terminal_map[prod] = new_nt
                    cnf[new_nt] = [prod]
                cnf[nt].append(terminal_map[prod])
            else:  # Valid CNF form
                new_prod = []
                for char in prod:
                    if char.islower():  # Replace terminal in mixed production
                        if char not in terminal_map:
                            new_nt = new_nonterminal()
                            terminal_map[char] = new_nt
                            cnf[new_nt] = [char]
                        new_prod.append(terminal_map[char])
                    else:
                        new_prod.append(char)
                cnf[nt].append(''.join(new_prod))

    return cnf


# Example CFG
cfg = {
    'S': ['AB', 'aB'],
    'A': ['a', 'aS'],
    'B': ['b', 'Sb']
}

# Convert to CNF
cnf = cfg_to_cnf(cfg)

# Print CNF
for nt, productions in cnf.items():
    print(f"{nt} -> {', '.join(productions)}")
