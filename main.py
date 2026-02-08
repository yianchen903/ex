import panda as pd
import numpy as np

def add(a,b):
    return a+b

print(add(2,3))

states = ['cal',"tex"]
popu = [20,40]
dict_sta = {'states':states, 'popu':popu}
dfsp = pd.DataFrame(dict_sta)
dfsp