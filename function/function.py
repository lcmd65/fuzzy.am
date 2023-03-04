import selenium as se
from fuzzywuzzy import fuzz
from solution.function.database_natural_lan import *

class fuzzy_score:
    def __init__(self):
        self.list = 

def fuzzy_attributes(meta_a, meta_b, alpha, beta):
    weight_a = fuzz(meta_a.tag_name, meta_b.tag_name)
    weight_b = fuzz(meta_a.value,meta_b.actual_value)
    
    score = (weight_a*alpha +weight_b*beta)/(alpha + beta)
    



