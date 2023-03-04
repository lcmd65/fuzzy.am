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
    
    def insertionSort(self):
        if (n := len(self.list)) <= 1: return
        for i in range(1, n):
            key = self.list[i]
            j = i-1
            while j >=0 and key.score < self.list[j].score :
                self.list[j+1] = self.list[j]
                j -= 1
            self.list[j+1] = key

def fuzzy_attributes(meta_a, meta_b, alpha, beta):
    weight_a = fuzz(meta_a.tag_name, meta_b.tag_name)
    weight_b = fuzz(meta_a.value,meta_b.actual_value)
    meta_a.score.append(item_score(meta_b.tag_name, weight_a * alpha + weight_b * beta)/(alpha + beta))

def processing():
    array_metadata_score = fuzzy_score()
    meta_controlplan = metadata_db_controlplan(370)
    meta_xml_1 = parse_metadata_xml(xml_global)
    meta_xml_2 = parse_metadata_xml(xml_recipe)
    for item in meta_controlplan:
        fuzzy_attributes
    
    



