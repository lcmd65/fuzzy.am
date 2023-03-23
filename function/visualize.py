import matplotlib.pyplot as plt 
import threading
from function.function_define import *

# plot alist of element that ever list have score of full data in lake
def plot_processing(array):
    p = plt.subplot(nrows = len(array.list), ncols =1)
    i = 0
    for item in array.list:
        p[i].title(item.tag_name, fontsize=17)
        p[i].plot(item.meta_data_lake_score, color = 'skyblue', linewidth=5)
        i+= 1

# parse a data structure in array class
def parseDataPhrase1(array):
    for item in array.list:
        dict_temp ={}
        for item_2 in item.meta_data_lake_score:
            dict_temp.update(item_2.name, item_2.score)
        print(item.tag_name, dict_temp)

# raw score list of 1 element list
def visualizePerUnit(list_temp):
    dict_temp ={}
    for item_2 in list_temp.meta_data_lake_score:
        dict_temp.update(item_2.name, item_2.score)
    
    p = plt.plot(dict_temp.score, dict_temp.name, color = 'skyblue')
    p.title(list_temp.tag_name, fontsize= 17)
    p.save(list_temp.tag_name)
    
# making a loop for all data with visualize _per_unit 
def loopPlotAttributeScore(array):
    for item in array:
        visualizePerUnit(item.list)

# Plotting a chart of a num of processing Attribute matching time
def loopPlotProcessingTime():

    

if __name__ == "__main__":
    arr = processing()
    parse_data(arr)
    
# python3 function/visualize.py
# tranfer a list to dictionary

