from cfg_parser import parse_cfg, print_cfg  # Import the print function for CFG
from pda_converter import convert_cfg_to_pda
from visualizer import visualize_pda

def main():
    grammar_lines = [
        "S -> aSb | ε"
    ]
    
    print("="*30)
    print("STEP 1: PARSING CFG")
    print("="*30)
    cfg = parse_cfg(grammar_lines)
    print_cfg(cfg)  # This shows the start symbol, terminals, etc.

    print("\n" + "="*30)
    print("STEP 2: CONVERTING TO PDA")
    print("="*30)
    pda = convert_cfg_to_pda(cfg)
    pda.display_pda()  # This prints the d(q_loop...) transitions

    print("\n" + "="*30)
    print("STEP 3: GENERATING VISUALIZATION")
    print("="*30)
    print("Generating window... (Close the window to finish)")
    
    visualize_pda(pda, r"PDA for $S \rightarrow aSb \mid \epsilon$")
    
    print("\nDone! Check 'pda_visualization.png' for the saved file.")

if __name__ == "__main__":
    main()