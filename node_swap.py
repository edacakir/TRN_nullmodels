# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 11:02:43 2020

@author: eda_c
"""

def node_swap(pos_dict, iter_per_node, dict_gene_operon, gene_alloperons):
    """
    Creates random graphs by node swapping
    graph : NetworkX Directed Graph
    iter_per_node : iteration per node (suggested: 100 iteration/node)
    gene_operon_dict : gene(key) - operon(value) dictionary to prevent any loops within the same operon
    
    return pos_dict_final, dict_gene_operon
    
    """
    
    import random
    
    
    num_nodes = len(pos_dict)
    iter_total=num_nodes*iter_per_node
    #iter_total = 10
    
    pos_dict_num={} #number instead of node name
    for i in range(len(pos_dict)):
        pos_dict_num[i]=list(pos_dict.values())[i]
    #print(pos_dict_num)    
    
    pos_dict_swap={} #number instead of pos data
    for i in range(len(pos_dict)):
        pos_dict_swap[list(pos_dict.keys())[i]]=i
    #print(pos_dict_swap)
    
    
    i=0
    while i < iter_total:
        #if i%10000 == 0: print(i)
        #two random number
        random_node_num1=random.randint(0, num_nodes-1)
        random_node_num2=random.randint(0, num_nodes-1)
        
        if random_node_num1==random_node_num2:
            continue
        
        #corresponding nodes
        random_node1=list(pos_dict_swap.keys())[random_node_num1]
        random_node2=list(pos_dict_swap.keys())[random_node_num2]
        
        #loops within operon not allowed
        if (dict_gene_operon[random_node1] in gene_alloperons[random_node2]
           )&(dict_gene_operon[random_node2] in gene_alloperons[random_node1]):        
            continue
        
        value1=pos_dict_swap[random_node1]
        value2=pos_dict_swap[random_node2]
        
        #swap values
        pos_dict_swap[random_node1]=value2
        pos_dict_swap[random_node2]=value1
        #print("{",random_node1, value2, "} {", random_node2, value1, "}")    
        i+=1
        
        #swap operons
        operon1=dict_gene_operon[random_node1]
        operon2=dict_gene_operon[random_node2]
        
        dict_gene_operon[random_node1]=operon2
        dict_gene_operon[random_node2]=operon1
        
    assert len(set(pos_dict_swap.values()))==len(pos_dict)
    
    pos_dict_final={}
    for i in range(len(pos_dict)):
        key=list(pos_dict_swap.keys())[i]
        num=pos_dict_swap[key]
        value=pos_dict_num[num]
        pos_dict_final[key]=value
        
    return pos_dict_final, dict_gene_operon