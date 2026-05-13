# Person 1: PDA Class and Data Structure
from cfg_parser import EPSILON, parse_cfg

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

def convert_cfg_to_pda(cfg):

    pda = PDA()
    # RULE 1: START TRANSITIONS
    pda.add_transition(
        'q_start',
        EPSILON,
        EPSILON,
        'q_push_start',
        [pda.stack_bottom]
    )

    pda.states.add('q_push_start')

    # then push Start Symbol S
    pda.add_transition(
        'q_push_start',
        EPSILON,
        EPSILON,
        'q_loop',
        [cfg.start_symbol]
    )    

   

    # RULE 2: EXPAND VARIABLES
        # RULE 2: EXPAND VARIABLES using intermediate states
    state_counter = 1

    for left in cfg.productions:

        for production in cfg.productions[left]:

            # epsilon production: A -> ε
            if production == [EPSILON]:
                pda.add_transition(
                    'q_loop',
                    EPSILON,
                    left,
                    'q_loop',
                    [EPSILON]
                )

            else:
                # reverse because stack push must happen from right to left
                push_symbols = production[::-1]

                current_state = 'q_loop'

                for i, symbol in enumerate(push_symbols):

                    # last symbol returns to q_loop
                    if i == len(push_symbols) - 1:
                        next_state = 'q_loop'
                    else:
                        next_state = f"q_mid_{state_counter}"
                        pda.states.add(next_state)
                        state_counter += 1

                    # first transition pops the non-terminal
                    if i == 0:
                        pop_symbol = left
                    else:
                        pop_symbol = EPSILON

                    pda.add_transition(
                        current_state,
                        EPSILON,
                        pop_symbol,
                        next_state,
                        [symbol]
                    )

                    current_state = next_state

    # RULE 3: MATCH TERMINALS
    for terminal in cfg.terminals:

        pda.add_transition(
            'q_loop',
            terminal,
            terminal,
            'q_loop',
            [EPSILON]
        )

    # RULE 4: ACCEPT    
    pda.add_transition(
        'q_loop',
        EPSILON,
        pda.stack_bottom,
        'q_accept',
        [EPSILON]
    )

    return pda

if __name__ == "__main__":

    grammar_lines = [
        "S -> aSb | ε"
    ]

    # Parse CFG
    cfg = parse_cfg(grammar_lines)

    # Convert CFG → PDA
    pda = convert_cfg_to_pda(cfg)

    # Display PDA
    pda.display_pda()