import sys
from cfg_parser import parse_cfg, print_cfg
from pda_converter import convert_cfg_to_pda
from visualizer import visualize_pda

def main():
    #The trial grammar
    grammar = ["S -> aSb | bSa | ε"]

    #Parser
    print("=" * 30 + "\nRUNNING cfg_parser.py\n" + "=" * 30, flush=True)
    cfg = parse_cfg(grammar)
    print_cfg(cfg) 
    sys.stdout.flush() # Forces VS Code Terminal to show text immediately

    #Converter
    print("\n" + "=" * 30 + "\nRUNNING pda_converter.py\n" + "=" * 30, flush=True)
    pda = convert_cfg_to_pda(cfg)
    pda.display_pda() 
    sys.stdout.flush()

    #Visualizer
    print("\n" + "=" * 30 + "\nRUNNING visualizer.py\n" + "=" * 30, flush=True)
    print("Generating Graphviz PDA visualization...", flush=True)
    
    visualize_pda(pda, "pda_result")

    print("\nPROCESS COMPLETED! Check 'pda_result.png' in your folder.", flush=True)
if __name__ == "__main__":
    main()