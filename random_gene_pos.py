# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 19:51:08 2020

@author: eda_c
"""

def random_gene_pos(gene_df):
      
      import random
      import numpy as np
      
      random_gene_pos=gene_df
      random_gene_pos["x_pos"]=""
      random_gene_pos["y_pos"]=""
        
      for i in range(len(random_gene_pos)):
          x=random.uniform(-1,1)
          random_gene_pos["x_pos"].iloc[i]=x
          y=np.sqrt(1-x**2)
      
          q=random.uniform(0,1)
          if q < 0.5: y=-y
              
          random_gene_pos["y_pos"].iloc[i]=y
        
      dict_random_gene_pos=random_gene_pos[["gene_name", "x_pos", "y_pos"]].set_index("gene_name").T.to_dict("list")
        
      return dict_random_gene_pos