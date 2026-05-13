import matplotlib.pyplot as plt
import networkx as nx

def parse_cfg(cfg_string):
    """Parses a CFG string like 'S -> aSa | bSb | ε' into rules and terminals."""
    rules = {}
    terminals = set()
    cfg_string = cfg_string.replace('e', 'ε')
    lines = [line.strip() for line in cfg_string.split('\n') if '->' in line]
    
    if not lines:
        return {}, set(), ""

    for line in lines:
        lhs, rhs_part = line.split('->')
        lhs = lhs.strip()
        productions = [p.strip() for p in rhs_part.split('|')]
        rules[lhs] = productions
        for p in productions:
            for char in p:
                if not char.isupper() and char != 'ε':
                    terminals.add(char)
    
    start_symbol = list(rules.keys())[0]
    return rules, terminals, start_symbol

def visualize_pda(cfg_input):
    rules, terminals, start_symbol = parse_cfg(cfg_input)
    if not rules:
        return

    G = nx.DiGraph()
    pos = {0: (0, 0), 1: (1, 0), 2: (2, 0)} 
    edge_labels = {}
    
    # 1. INITIALIZATION
    G.add_edge(0, 1)
    edge_labels[(0, 1)] = "ε, ε → $"
    G.add_edge(1, 2)
    edge_labels[(1, 2)] = f"ε, ε → {start_symbol}"
    
    current_idx = 3
    loop_labels_list = []

    # 2. VARIABLE EXPANSIONS
    y_offset = 1.0
    for var, prods in rules.items():
        for prod in prods:
            if prod == 'ε':
                loop_labels_list.append(f"ε, {var} → ε")
                continue
            
            symbols = list(prod)
            first_push = symbols.pop()
            
            G.add_edge(2, current_idx)
            pos[current_idx] = (3, y_offset)
            edge_labels[(2, current_idx)] = f"ε, {var} → {first_push}"
            
            prev = current_idx
            current_idx += 1
            while symbols:
                nxt_push = symbols.pop()
                G.add_edge(prev, current_idx)
                pos[current_idx] = (pos[prev][0] + 0.8, y_offset)
                edge_labels[(prev, current_idx)] = f"ε, ε → {nxt_push}"
                prev = current_idx
                current_idx += 1
            
            G.add_edge(prev, 2)
            y_offset -= 0.8

    # 3. TERMINALS (Purple Loop)
    for t in sorted(terminals):
        loop_labels_list.append(f"{t}, {t} → ε")
    
    # Explicit self-loop for visualization
    G.add_edge(2, 2)
    # Filter to ensure we focus on the specific purple lines mentioned
    edge_labels[(2, 2)] = "\n".join(loop_labels_list)
    
    # 4. ACCEPTANCE
    accept_state = current_idx
    G.add_edge(2, accept_state)
    pos[accept_state] = (1.2, -1.2)
    edge_labels[(2, accept_state)] = "ε, $ → ε"

    # --- DRAWING ---
    plt.figure(figsize=(16, 12))
    
    # Draw Nodes
    regular_nodes = [n for n in G.nodes if n != accept_state]
    nx.draw_networkx_nodes(G, pos, nodelist=regular_nodes, node_size=2800, 
                           node_color="white", edgecolors="black", linewidths=2)
    nx.draw_networkx_nodes(G, pos, nodelist=[accept_state], node_size=2800, 
                           node_color="white", edgecolors="black", linewidths=2)
    nx.draw_networkx_nodes(G, pos, nodelist=[accept_state], node_size=2000, 
                           node_color="white", edgecolors="black", linewidths=1.2)

    nx.draw_networkx_labels(G, pos, labels={n: f"q{n}" for n in G.nodes}, font_size=13, font_weight='bold')

    # --- DRAW EDGES WITH MASSIVE LOOP ON Q2 ---
    for u, v in G.edges():
        if u == 2 and v == 2:
            # INCREASED RAD for a much larger "circle" arrow
            connection = "arc3,rad=3.5" 
            edge_width = 10
            arrow_size = 10
        else:
            connection = "arc3,rad=0.3" if (v == 2 and u > 2) else "arc3,rad=0"
            edge_width = 2.0
            arrow_size = 40
        
        nx.draw_networkx_edges(
            G, pos, edgelist=[(u, v)], 
            arrowstyle='-|>',  
            arrowsize=arrow_size,
            width=edge_width, 
            connectionstyle=connection,
            edge_color="black",
            min_source_margin=20,
            min_target_margin=20
        )

    # DRAW ALL LABELS
    for (u, v), label in edge_labels.items():
        if u == 2 and v == 2:
            # Positioning the purple text inside the massive loop
            plt.text(pos[2][0], pos[2][1] + 1.2, label, 
                     ha='center', fontsize=11, color="purple", fontweight='bold',
                     bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))
        else:
            nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): label}, 
                                         font_size=10, rotate=False, label_pos=0.5)

    # Footer Steps (Purple)
    steps = [
        "Steps:",
        "• Push $ to Stack",
        "• Push Start Symbol to stack",
        "• Pop/Push Variables in the main loop",
        "• Pop/Push terminals in the main loop",
        "• Match $ to move to accept state"
    ]
    plt.text(-0.5, -2.5, "\n".join(steps), fontsize=14, color="purple", va='bottom', fontweight='bold')

    plt.axis('off')
    plt.tight_layout()
    plt.show()

user_cfg = "S -> aSa | bSb | ε"
visualize_pda(user_cfg)