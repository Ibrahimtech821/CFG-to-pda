import sys
from cfg_parser import parse_cfg, print_cfg
from pda_converter import convert_cfg_to_pda
from visualizer import visualize_pda

def main():
    grammar_lines = [
        "S -> aSb | A"
    ]
    cfg_input = "\n".join(grammar_lines)

    # --- STEP 1: cfg_parser.py ---
    print("=" * 30, flush=True)
    print("RUNNING cfg_parser.py", flush=True)
    print("=" * 30, flush=True)
    cfg = parse_cfg(grammar_lines)
    print_cfg(cfg) # This calls the print logic inside your parser file
    sys.stdout.flush() # Forces Ubuntu to show the text NOW

    # --- STEP 2: pda_converter.py ---
    print("\n" + "=" * 30, flush=True)
    print("RUNNING pda_converter.py", flush=True)
    print("=" * 30, flush=True)
    pda = convert_cfg_to_pda(cfg)
    pda.display_pda() # This calls the print logic inside your converter file
    sys.stdout.flush()

    # --- STEP 3: visualizer.py ---
    print("\n" + "=" * 30, flush=True)
    print("RUNNING visualizer.py", flush=True)
    print("=" * 30, flush=True)
    print("Generating window... (Close the window to finish)", flush=True)
    sys.stdout.flush()
    
    # This opens the GUI window
    visualize_pda(cfg_input)
    
    print("\nDone! All steps completed.", flush=True)

if __name__ == "__main__":
    main()