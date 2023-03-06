import matplotlib.pyplot as plt
from function.function import *

def plot_processing():
    array = processing()
    p = plt.subplot(nrows = len(array.list), ncols =1)
    index = len(array.list)
    i = 0
    for item in array.list:
        p[i].title(item.list.name, fontsize=17)
        p[i].plot(item.list.score, color='skyblue', linewidth=5)
        i+=1
        
if __name__ == "__main__":
    plot_processing()

#python3 function/visualize.py
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