# -*- coding: utf-8 -*-
"""
Created on Sun May 23 00:49:52 2021

@author: Rafae
"""

import json
import ast

def Write(FileName, contents):
    f = open(FileName, "a")
    f.writelines(json.dumps(contents))
    f.write("\n")
    f.close()
    
def Overwrite(FileName, contents):
    f = open(FileName, "w")
    f.writelines(json.dumps(contents))
    f.write("\n")
    f.close()

def Read(Filename):
    with open(Filename, "r") as f:
        for last_line in f: 
            pass
    return ast.literal_eval(last_line)