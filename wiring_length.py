# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 10:55:39 2020

@author: eda_c
"""

def wiring_length(graph, pos_dict):
    """
    Calculates total wiring length of the graph
    
    """
    
    import networkx as nx
    import numpy as np
    
    edgelist=nx.to_pandas_edgelist(graph)
    total_wiring_length=0

    for i in range(len(edgelist)):
        source_node=edgelist.iloc[i, 0]
        target_node=edgelist.iloc[i, 1]
        sn_pos=pos_dict[source_node]
        tn_pos=pos_dict[target_node]
        wiring_length=np.sqrt((sn_pos[0]-tn_pos[0])**2+(sn_pos[1]-tn_pos[1])**2)
        total_wiring_length += wiring_length
                    
    return round(total_wiring_length,2)