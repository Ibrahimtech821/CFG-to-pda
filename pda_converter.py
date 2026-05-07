# Person 1: PDA Class and Data Structure
from cfg_parser import EPSILON

class PDA:
    def __init__(self):
        # Define the set of states
        self.states = {'q_start', 'q_loop', 'q_accept'}
        self.start_state = 'q_start'
        self.accept_state = 'q_accept'
        self.stack_bottom = '$'
        self.transitions = []

    def add_transition(self, from_state, input_char, pop_char, to_state, push_list):
        """
        Standard transition format: (Current State, Input, Pop) -> (Next State, Push)
        push_list: a list of symbols to be pushed onto the stack
        """
        self.transitions.append({
            'from': from_state,
            'input': input_char,
            'pop': pop_char,
            'to': to_state,
            'push': push_list
        })

    def display_pda(self):
        """Prints the PDA components in a readable format"""
        print(f"--- PDA Transition Functions ---")
        for t in self.transitions:
            # Convert list ['a', 'S', 'b'] to string "aSb" for display
            push_val = "".join(t['push']) if t['push'] != [EPSILON] else EPSILON
            print(f"d({t['from']}, {t['input']}, {t['pop']}) -> ({t['to']}, {push_val})")

# ==============================================================
# TODO FOR PERSON 2: IMPLEMENT THE CONVERSION LOGIC
# ==============================================================
# Use the 'pda.add_transition' method to follow these 4 rules:
#
# 1. START: Move from 'q_start' to 'q_loop' and push (Start Symbol + '$').
#
# 2. EXPAND: For each CFG rule like (A -> bC), create a transition 
#    that pops 'A' and pushes 'bC' while staying in 'q_loop'.
#
# 3. MATCH: For each terminal (like 'a' or 'b'), create a transition 
#    that reads the character from input and pops it from the stack.
#
# 4. FINISH: When you see '$' on the stack, move to 'q_accept'.
# ==============================================================
