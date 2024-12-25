def cfg_to_cnf(cfg):
    new_cfg = {}
    counter = 1

    for nt, productions in cfg.items():
        new_cfg[nt] = []
        for prod in productions:
            if len(prod) > 2:  # Break long productions
                while len(prod) > 2:
                    new_nt = f"X{counter}"
                    counter += 1
                    new_cfg[new_nt] = [prod[:2]]
                    prod = new_nt + prod[2:]
                new_cfg[nt].append(prod)
            elif len(prod) == 1 and prod.islower():  # Replace terminals in single rules
                new_nt = f"X{counter}"
                counter += 1
                new_cfg[new_nt] = [prod]
                new_cfg[nt].append(new_nt)
            else:
                new_cfg[nt].append(prod)

    return new_cfg

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