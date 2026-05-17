
EPSILON = "ε"


class CFG:
    def __init__(self, start_symbol, productions,
                 terminals, non_terminals):

        self.start_symbol = start_symbol
        self.productions = productions
        self.terminals = terminals
        self.non_terminals = non_terminals


def parse_cfg(lines):

    productions = {}
    non_terminals = set()
    terminals = set()

    start_symbol = None

    # FIRST PASS
    # collect non terminals from left side

    for line in lines:

        line = line.strip()

        if line == "":
            continue

        left, right = line.split("->")

        left = left.strip()

        non_terminals.add(left)

        if start_symbol is None:
            start_symbol = left

    # SECOND PASS
    # build productions and terminals

    for line in lines:

        line = line.strip()

        if line == "":
            continue

        if "->" not in line:
            raise ValueError("Invalid CFG format")

        left, right = line.split("->")

        left = left.strip()
        right = right.strip()

        alternatives = right.split("|")

        if left not in productions:
            productions[left] = []

        for alt in alternatives:

            alt = alt.strip()

            # epsilon
            if alt == EPSILON or alt == "e" or alt == "":
                productions[left].append([EPSILON])

            else:

                symbols = []

                for char in alt:

                    if char == " ":
                        continue

                    symbols.append(char)

                    if char not in non_terminals:
                        terminals.add(char)

                productions[left].append(symbols)

    terminals.discard(EPSILON)

    return CFG(
        start_symbol,
        productions,
        terminals,
        non_terminals
    )


def print_cfg(cfg):

    print("\nSTART SYMBOL:")
    print(cfg.start_symbol)

    print("\nNON TERMINALS:")
    print(cfg.non_terminals)

    print("\nTERMINALS:")
    print(cfg.terminals)

    print("\nPRODUCTIONS:")

    for left in cfg.productions:

        print(left, "->", cfg.productions[left])


if __name__ == "__main__":

    grammar_lines = [
        "S -> aSb | T",
        "A -> aA | b",
        "T-> nTs|S"
    ]

    cfg = parse_cfg(grammar_lines)

    print_cfg(cfg)