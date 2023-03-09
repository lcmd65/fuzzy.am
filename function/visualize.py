import matplotlib.pyplot as plt
from function.function import *

def plot_processing(array):
    p = plt.subplot(nrows = len(array.list), ncols =1)
    i = 0
    for item in array.list:
        p[i].tittle(item.tag_name, fontsize=17)
        p[i].plot(item.meta_data_lake_score, color = 'skyblue', linewidth=5)
        i+= 1

def parse_data(array):
    i = 0
    for item in array.list:
        dict_temp ={}
        for item_2 in item.meta_data_lake_score:
            dict_temp.update(item_2.name, item_2.score)
        print(item.tag_name, dict_temp)

if __name__ == "__main__":
    arr = processing()
    parse_data(arr)
    
# python3 function/visualize.py
# tranfer a list to dictionary

#structure of data (data ogarnize in program)
# array.list {
    # 
        #med_data_db {
            #meta_data_db.tag_name
            #meta_data_db.meta_data_lake_score {
                #item_score{
                    #item_score.name
                    #item_score.score
                #}
            #}
        #}
    #}
#}