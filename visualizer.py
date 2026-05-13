import matplotlib.pyplot as plt
import networkx as nx

def visualize_pda(pda, title_text):
    G = nx.DiGraph()
    nodes = {"q_start": (0, 0), "q_loop": (2, 0), "q_accept": (4, 0)}
    G.add_nodes_from(nodes.keys())

    plt.figure(figsize=(10, 6))
    
    plt.text(2, 1.3, title_text, 
             fontsize=18, ha='center', fontweight='bold', color="#333333")

    node_colors = ["#42f59e", "#6bcbef", "#ffadd2"]
    nx.draw_networkx_nodes(G, nodes, node_color=node_colors, node_size=2500, edgecolors='black')
    nx.draw_networkx_labels(G, nodes, font_weight='bold')

    plt.annotate("", xy=(1.75, 0), xytext=(0.25, 0),
                 arrowprops=dict(arrowstyle="->", color="black", lw=1.5, connectionstyle="arc3,rad=0.1"))
    plt.text(1, 0.15, "ε, ε → S$", ha='center', fontsize=11)

    plt.annotate("", xy=(3.75, 0), xytext=(2.25, 0),
                 arrowprops=dict(arrowstyle="->", color="black", lw=1.5, connectionstyle="arc3,rad=0.1"))
    plt.text(3, 0.15, "ε, $ → ε", ha='center', fontsize=11)

    plt.annotate("", 
                 xy=(2.1, 0.15),      
                 xytext=(1.9, 0.15),   
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-4.5", 
                                 color="black", lw=1.5))
    
    plt.text(2, 0.85, 
             "Expansion Rules:\n"
             "δ(q_loop, ε, S) → (q_loop, aSb)\n"
             "δ(q_loop, ε, S) → (q_loop, ε)\n\n"
             "Matching Rules:\n"
             "δ(q_loop, a, a) → (q_loop, ε)\n"
             "δ(q_loop, b, b) → (q_loop, ε)",
             ha='center', fontsize=9,
             bbox=dict(boxstyle="round,pad=0.5", fc="white", ec="#cccccc", alpha=0.9))

    plt.xlim(-1, 5)
    plt.ylim(-0.5, 1.8)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig("pda_visualization.png", dpi=300, bbox_inches='tight')
    plt.show()