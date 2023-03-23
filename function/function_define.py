from fuzzywuzzy import fuzz
from function.database_natural_lan import *
import time 

class item_score:
    def __init__(self,name, score):
        self.name = name
        self.score = score 
        # use dictionary here

class fuzzy_score:
    def __init__(self): # init arr
        self.list = []
    
    def push_meta(self, meta_data): # push item
        self.list.append(meta_data)
    
    def insertion_sort(self): # sort the score array after fitting with fuzzy matching
        for item in self.list:
            if (n := len(item.meta_data_lake_score)) <= 1: 
                return
            for index in range(1, n):
                key = item.meta_data_lake_score[index]
                jindex = index-1
                while jindex >=0 and key.score < item.meta_data_lake_score[jindex].score :
                    item.meta_data_lake_score[jindex+1] = item.meta_data_lake_score[jindex]
                    jindex -= 1
                item.meta_data_lake_score[jindex+1] = key

def fuzzy_attributes(meta_a, meta_b, alpha, beta): # unit caculate of fuzzy matching 
    weight_a = fuzz(meta_a.tag_name, meta_b.tag_name)
    weight_b = fuzz(meta_a.value,meta_b.actual_value)
    return item_score((meta_b.tag_name, weight_a * alpha + weight_b * beta)/(alpha + beta))

def main_processing(): # parsing and caculate score of fuzzy matching
    array_metadata_score = fuzzy_score()
    meta_controlplan = metadata_db_controlplan(370)
    meta_xml_1 = parse_metadata_xml(xml_global)
    meta_xml_2 = parse_metadata_xml(xml_recipe)
    for item in meta_controlplan:
        for item_item in meta_xml_1:
            item.meta_data_lake_score.append(fuzzy_attributes(item, item_item, 0.7, 0.3))
        for item_item_2 in meta_xml_2:
            item.meta_data_lake_score.append(fuzzy_attributes(item, item_item_2, 0.7, 0.3))
        array_metadata_score.push_meta(item)
    array_metadata_score.insertion_sort()
    return array_metadata_score

def compareAfterImprovement():
    global list_file
    print("____________Start____________")
    start = time.time()
    main_processing()
    elapsed = time.time() - start
    list_file.append(elapsed) 
    return list_file


