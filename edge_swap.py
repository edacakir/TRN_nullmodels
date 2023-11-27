# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 10:58:49 2020

@author: eda_c
"""

def edge_swap(graph, iter_per_edge, gene_operon_dict):
    """
    Creates random graphs by edge swapping
    graph : NetworkX Directed Graph
    iter_per_edge : iteration per edge (suggested: 100 iteration/edge)
    gene_operon_dict : gene(key) - operon(value) dictionary to prevent any loops within the same operon
    
    """
    import random
    import networkx as nx
    
    new_graph=graph.copy()
    edges=list(new_graph.edges())
    num_edges = new_graph.number_of_edges()
    iter_total=num_edges*iter_per_edge
    out_degree_original = list(graph.out_degree())
    i=0
    while i < iter_total:
        random_edge_1=random.randint(0, num_edges-1)
        random_edge_2=random.randint(0, num_edges-1)
        edge_1_original = edges[random_edge_1]
        edge_2_original = edges[random_edge_2]
        #print(i)
        #print("original: {} {}".format(edge_1_original, edge_2_original))
        source_node_1, target_node_1 = edge_1_original
        source_node_2, target_node_2 = edge_2_original
        
        #prevent gene to gene self-loops
        if (source_node_1 == target_node_2) | (source_node_2==target_node_1):
            continue
        #results in same edge
        if (source_node_1 == source_node_2) | (target_node_1==target_node_2):
            continue
        #generated edge exists
        if new_graph.has_edge(source_node_1, target_node_2) | new_graph.has_edge(
                source_node_2, target_node_1):
            continue
        #prevent operon to operon self loops
        if (gene_operon_dict[source_node_1]==gene_operon_dict[target_node_2]) | (gene_operon_dict[
            source_node_2]==gene_operon_dict[target_node_1]):
            continue
            
        #remove original edges from graph
        new_graph.remove_edges_from([edge_1_original, edge_2_original])
        
        #create new edges by swapping
        edge_1_new = (source_node_1, target_node_2)
        edge_2_new = (source_node_2, target_node_1)
        #print("new: {} {}".format(edge_1_new, edge_2_new))
        
        #add new edges to graph
        new_graph.add_edges_from([edge_1_new, edge_2_new])
        edges[random_edge_1]=edge_1_new
        edges[random_edge_2]=edge_2_new
        i+=1
        #print(i)
    assert list(new_graph.out_degree()) == out_degree_original
    return new_graph 