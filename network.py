import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def network_rules(rules, display_rules):
    
    """
    The function plots a network graph of antecedents and consequents
    It takes in datasets and number of values to be displayed ad inputs
    
    
    Inputs: 
           rules: The rule table created by performing the association rules 
           
           display_rules: number of values to be displayed.
           
    Output:
            A Network plot of antecedents and consequents.
            
    
    """
    #Instantiate the graph
    G = nx.DiGraph()
    
    color_map = []
    N = 50
    colors = np.random.rand(N)    
    rule_strs = ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6']   
    
    # Define the nodes and edges
    for i in range(display_rules):      
        G.add_nodes_from(["R"+str(i)])
    
        for a in rules.iloc[i]['antecedents']:
            G.add_nodes_from([a])
            G.add_edge(a, "R"+str(i), color=colors[i], weight=3)
       
        for c in rules.iloc[i]['consequents']:
            G.add_nodes_from([a])
            G.add_edge("R"+str(i), c, color=colors[i], weight=3)
            
     # Define the color map for the nodes 
    for node in G:
        color_map.append('skyblue' if node in rule_strs else 'red')
    
    # Define zthe network layout
    pos = nx.kamada_kawai_layout(G, scale=2.0)
    
    # Create a Matplotlib figure and axis
    fig, ax = plt.subplots(figsize=(15,7))
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=300, node_color=color_map, ax=ax)
    
    # Draw edges
    for (i, j, k) in G.edges(data=True):
        edge_color = [k['color']]  # Convert edge color to a list
        nx.draw_networkx_edges(G, pos, edgelist=[(i, j)], edge_color=edge_color, width=k['weight'], ax=ax)
    
    # Draw labels
    nx.draw_networkx_labels(G, pos, ax=ax)
    
    # Show the plot
    return plt.show()

