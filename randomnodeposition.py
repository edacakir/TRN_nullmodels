# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 21:04:05 2020

@author: eda_c
"""

def randomnodeposition(graph, operon_position_data):
      
      import random
      import numpy as np
      import pandas as pd
      import networkx as nx
      from numpy import pi, sin, cos
      
      #determine operon limits
      operon_position_data=operon_position_data.sort_values("gene_posleft").reset_index(drop=True)
      operon_position_data["limit"]=""
      
      for i in range(len(operon_position_data)-1):
            if (operon_position_data.gene_posright.iloc[i]>operon_position_data.gene_posleft.iloc[i+1]):
                  diff=(operon_position_data.gene_posright.iloc[i]-operon_position_data.gene_posleft.iloc[i+1])/2
                  operon_position_data.limit.iloc[i]=operon_position_data.gene_posright.iloc[i]-diff
            else:
                  diff=(-operon_position_data.gene_posright.iloc[i]+operon_position_data.gene_posleft.iloc[i+1])/2
                  operon_position_data.limit.iloc[i]=operon_position_data.gene_posright.iloc[i]+diff
      operon_position_data.limit.iloc[len(operon_position_data)-1]=operon_position_data.gene_posright.iloc[len(operon_position_data)-1]
      
      operon_position_data["limit"]=pd.to_numeric(operon_position_data["limit"])

            
      #dataframe to save solution
      random_gene_pos=pd.DataFrame(graph.nodes()).rename(columns={0:"gene_name"})
      random_gene_pos["operon"]=""
      random_gene_pos["x_pos"]=""
      random_gene_pos["y_pos"]=""
      random_gene_pos["pos_center"]=""
      random_gene_pos["operon_id"]=""
            
      for i in range(len(random_gene_pos)):
            random_gene_pos["operon"].iloc[i]="Operon"+str(i+1)
 
      
      #regulation dataframe
      reg_list=pd.DataFrame(graph.edges()).rename(columns={0:"gene_name_regulator", 1:"gene_name_regulated"})
      reg_list=pd.merge(left=reg_list, right= random_gene_pos[["gene_name", "operon"]], how="left", 
                        left_on="gene_name_regulator", right_on="gene_name", left_index=False , right_index=False)
      reg_list=pd.merge(left=reg_list, right= random_gene_pos[["gene_name", "operon"]], how="left", 
                        left_on="gene_name_regulated", right_on="gene_name", left_index=False , right_index=False)
      reg_list=reg_list[['gene_name_regulator', 'gene_name_regulated', 'operon_x', 'operon_y']]
      
      #dictionary - genes as keys - all related operons as values
      alloperons={}
      for i, gene_row in random_gene_pos.iterrows():
            gene = gene_row[0]
            regulators = reg_list[reg_list["gene_name_regulated"]==gene].operon_x.to_list()
            regulatees = reg_list[reg_list["gene_name_regulator"]==gene].operon_y.to_list()
            regulators.extend(regulatees)
            alloperons[gene]=regulators


      i=0
      while i < len(random_gene_pos):
            theta = random.random() 
            x = cos(theta* 2 * pi)
            y = sin(theta* 2 * pi)
        
            pos_cen = 4641628.0*theta
        
            opr=operon_position_data["operon_id"].iloc[len(operon_position_data[operon_position_data["limit"] <pos_cen])]
            
            if opr in alloperons[random_gene_pos["gene_name"].iloc[i]]:
                continue
            else:
                  random_gene_pos["x_pos"].iloc[i]=x    
                  random_gene_pos["y_pos"].iloc[i]=y
                  random_gene_pos["pos_center"].iloc[i]=pos_cen
                  random_gene_pos["operon_id"].iloc[i]=opr        
                  
                  for key,value in alloperons.items():
                        if random_gene_pos["operon"].iloc[i] in value:
                              value.remove(random_gene_pos["operon"].iloc[i])
                              value.append(opr)
                  
                  i+=1
      
      new_pos_dict=random_gene_pos[["gene_name", "x_pos", "y_pos"]].set_index("gene_name").T.to_dict("list")
      new_gene_operon=random_gene_pos[["gene_name", "operon_id"]]
            
      
      return new_pos_dict, new_gene_operon