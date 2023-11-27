# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 10:38:25 2020

@author: eda_c
"""

def wiringlength_and_connectivity(graph, pos_dict):
    '''
    calculates below values of a graph:
    out-degree, in-degree, descendant number, average total path length, average path length
    
    requires networkx
    
    returns wiring length and connectivity values
    '''
    import networkx as nx
    import numpy as np
    import pandas as pd
    
    from wiring_length import wiring_length
    from wiring_length_1D import wiring_length_1D
    
    new_graph=graph.copy()
    
    #out degree
    out_dic= dict(new_graph.out_degree())
    regulator_dict= {k:v for (k,v) in out_dic.items() if v > 0}
    #out_deg = [i for i in list(out_dic.values())]
         
    #in-degree
    in_dic=dict(new_graph.in_degree())
    #in_deg = [i for i in list(in_dic.values())]
        
    assert [i for i in list(out_dic.keys())]==[i for i in list(in_dic.keys())]
    
    #degree = np.mean(list(dict(new_graph.degree()).values()))
    #out_in_list=[x/y for x, y in zip(out_deg, in_deg) if (y!=0) & (x!=0)]
    #out_in = np.mean(out_in_list)
    
    #average descendant number
    descendant_num = []
    for i in regulator_dict.keys():
        descendant_num.append(len(nx.descendants(new_graph, i)))
    descendant_number_avg = np.mean(descendant_num)
    #descendant_number_min = np.min(descendant_num)
    #descendant_number_max = np.max(descendant_num)
    
    #average total path length
    length=dict(nx.all_pairs_shortest_path_length(new_graph))
    length_df=pd.DataFrame.from_dict(length, orient='index')
    total_path_lengths=[i for i in length_df.sum(axis=1) if i != 0]
    total_path_length_avg=np.mean(total_path_lengths)
    #total_path_length_min=np.min(total_path_lengths)
    #total_path_length_max=np.max(total_path_lengths)
    
    #average path length
    path_length_avg = total_path_length_avg/descendant_number_avg
    
    #wiring length
    wl = wiring_length(new_graph, pos_dict)
    wl1 = wiring_length_1D(new_graph, pos_dict)
    
    df = pd.DataFrame([[
        #degree,
        #out_in,
        descendant_number_avg,
        #descendant_number_max,
        #total_path_length_min, 
        total_path_length_avg,
        #total_path_length_max,
        path_length_avg,
        wl, wl1]]
                      , columns=[
                          #"graph_degree",
                          #"out/in degree",
                          "descendant_number_avg",
                          #"descendant_number_max",
                          #"total_path_length_min",
                          "total_path_length_avg",
                          #"total_path_length_max",
                          "trn_aspl",
                          "trn_wiringlength_2D",
                          "trn_wiringlength_1D"])
    return df