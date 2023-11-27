# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 21:04:05 2020

@author: eda_c
"""

def operon_randomnodeposition(graph):
      
      import random
      #import numpy as np
      import pandas as pd
      import networkx as nx
      from numpy import pi, sin, cos
           
      #dataframe to save solution
      random_operon_pos=pd.DataFrame(graph.nodes()).rename(columns={0:"operon_name"})
      random_operon_pos["x_pos"]=""
      random_operon_pos["y_pos"]=""

      for i in range(len(random_operon_pos)):
            theta = random.random() 
            x = cos(theta* 2 * pi)
            y = sin(theta* 2 * pi)
   
            random_operon_pos["x_pos"].iloc[i]=x    
            random_operon_pos["y_pos"].iloc[i]=y

      for i in [1,2]:
            random_operon_pos.iloc[:,i]=pd.to_numeric(random_operon_pos.iloc[:,i], downcast='float')

      
      new_pos_dict=random_operon_pos[["operon_name",
                                      "x_pos",
                                      "y_pos"]].set_index("operon_name").T.to_dict("list")            
      
      return new_pos_dict