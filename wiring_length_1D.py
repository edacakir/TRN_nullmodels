# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 10:57:07 2020

@author: eda_c
"""

def wiring_length_1D(graph, pos_dict):
    """
    Calculates total 1D wiring length of the graph
    takes the min 1D distance
    """
    import networkx as nx
    import numpy as np
    
    edgelist=list(graph.edges())
    total_wiring_length=0

    for i in range(len(edgelist)):
        source_node, target_node = edgelist[i]
        sn_pos=pos_dict[source_node]
        tn_pos=pos_dict[target_node]
        wiring_length=np.arccos(np.dot(sn_pos, tn_pos))
        if np.isnan(wiring_length):
              continue
        else:
              total_wiring_length += wiring_length
                    
    return round(total_wiring_length,2)