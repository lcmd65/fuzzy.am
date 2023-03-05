import selenium as se
from fuzzywuzzy import fuzz
from solution.function.database_natural_lan import *

class item_score:
    def __init__(self,name, score):
        self.name = name
        self.score = score 

class fuzzy_score:
    def __init__(self):
        self.list = []
    
    def push_meta(self, meta_data):
        self.list.append(meta_data)
    
    def insertion_sort(self):
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

def fuzzy_attributes(meta_a, meta_b, alpha, beta):
    weight_a = fuzz(meta_a.tag_name, meta_b.tag_name)
    weight_b = fuzz(meta_a.value,meta_b.actual_value)
    return item_score((meta_b.tag_name, weight_a * alpha + weight_b * beta)/(alpha + beta))

def processing():
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
    



