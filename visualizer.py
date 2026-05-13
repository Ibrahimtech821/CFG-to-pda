from graphviz import Digraph
from cfg_parser import EPSILON

def build_state_mapping(pda):
    ordered_states = [pda.start_state]
    if getattr(pda, 'start_state', None) != getattr(pda, 'accept_state', None):
        if 'q_push_start' in pda.states:
            ordered_states.append('q_push_start')
        if 'q_loop' in pda.states:
            ordered_states.append('q_loop')
    mid_states = [s for s in pda.states if s not in ordered_states + [pda.accept_state]]
    def mid_key(name):
        if name.startswith('q_mid_'):
            try:
                return (0, int(name.split('_')[-1]))
            except ValueError:
                return (0, name)
        return (1, name)
    mid_states = sorted(mid_states, key=mid_key)
    ordered_states.extend(mid_states)
    if pda.accept_state not in ordered_states:
        ordered_states.append(pda.accept_state)
    return {old: f"q{i}" for i, old in enumerate(ordered_states)}
def visualize_pda(pda, output_file="pda_visualization"):
    mapping = build_state_mapping(pda)

    dot = Digraph(format='png', graph_attr={'rankdir': 'LR'})
    dot.attr('node', style='filled', fontname='Arial', fontsize='10')
    for old, new in mapping.items():
        is_accept = (old == pda.accept_state)
        is_start = (old == pda.start_state)
        fillcolor = 'lightgreen' if is_start else ('lightyellow' if is_accept else 'lightblue')
    
        dot.node(
            new, new,
            shape='doublecircle' if is_accept else 'circle',
            fillcolor=fillcolor
        )
    dot.node('start_ptr', shape='point', width='0')
    dot.edge('start_ptr', mapping[pda.start_state])

    edge_labels = {}
    for t in pda.transitions:
        u = mapping[t['from']]
        v = mapping[t['to']]
        if t['push'] == [EPSILON]:
            push_str = EPSILON
        else:
            push_str = "".join(t['push'])

        label = f"{t['input']}, {t['pop']} → {push_str}"
        edge_labels.setdefault((u, v), []).append(label)
    for (u, v), labels in edge_labels.items():
        combined_label = "\n".join(labels)
        dot.edge(u, v, label=combined_label, fontsize='9')
    dot.render(output_file, cleanup=True)
    print(f"✓ PDA saved as {output_file}.png (Accept state: {mapping[pda.accept_state]})", flush=True)