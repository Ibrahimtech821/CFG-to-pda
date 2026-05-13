from cfg_parser import parse_cfg, print_cfg
from pda_converter import convert_cfg_to_pda
from visualizer import visualize_pda


def get_cfg_from_user():
    print("Enter CFG rules one by one.")
    print("Example: S -> aSb | ε")
    print("Write 'done' when finished.\n")

    grammar_lines = []

    while True:
        line = input("Rule: ")

        if line.lower() == "done":
            break

        grammar_lines.append(line)

    return grammar_lines


def main():
    grammar_lines = get_cfg_from_user()

    cfg = parse_cfg(grammar_lines)


    pda = convert_cfg_to_pda(cfg)


    print("\n========== GRAPHVIZ ==========")
    visualize_pda(pda, "pda_graph")


if __name__ == "__main__":
    main()