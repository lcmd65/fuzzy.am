from fuzzywuzzy import fuzz
from function.database_natural_lan import * # weight_element1, weight_element2
import time 

# item score define
class item_score:
    def __init__(self,name, score):
        self.name = name
        self.score = score 
        # use dictionary here

# fuzzy score object define
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

# unit caculate of fuzzy matching 
def fuzzyAttributes(meta_a, meta_b, alpha, beta):
    weight_a = fuzz(meta_a.tag_name, meta_b.tag_name)
    weight_b = fuzz(meta_a.value,meta_b.actual_value)
    return item_score((meta_b.tag_name, weight_a * alpha + weight_b * beta)/(alpha + beta))

# parsing and caculate score of fuzzy matching
def mainProcessing(weight_element1, weight_element2):
    array_metadata_score = fuzzy_score()
    meta_controlplan = metadata_db_controlplan(370)
    meta_xml_1 = parse_metadata_xml(xml_global)
    meta_xml_2 = parse_metadata_xml(xml_recipe)
    for item in meta_controlplan:
        for item_item in meta_xml_1:
            item.meta_data_lake_score.append(fuzzyAttributes(item, item_item, weight_element1, weight_element2))
        for item_item_2 in meta_xml_2:
            item.meta_data_lake_score.append(fuzzyAttributes(item, item_item_2, weight_element1, weight_element2))
        array_metadata_score.push_meta(item)
    array_metadata_score.insertion_sort()
    return array_metadata_score

# function caculate time processing of main algorithms (expect < 1 min for all tasks)
def compareAfterImprovement():
    list_file = []
    print("____________Start____________")
    start = time.time()
    mainProcessing(string_weight_element1, string_weight_element2s))
    elapsed = time.time() - start
    list_file.append(elapsed) 
    return list_file
