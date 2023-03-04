import pymssql
import pandas as pd
import xml.etree.cElementTree as ET
from function.string import * 

meta_data_natural = []
class root_metadata:
    def __init__(self):
        self.meta_data_lake = []
        self.size = 0

class meta_data_xml:
    def __init__(self, tag_name, actual_value):
        self.tag_name = tag_name
        self.actual_value = actual_value

class meta_data_db:
    def __init__(self, tag_name, value):
        self.tag_name = tag_name
        self.value = value

def metadata_db_controlplan(size):
    global meta_data_temp
    cnxn = pymssql.connect(server= HOST, port= PORT\
                        , database= DB_GET\
                        , user= USER\
                        , password= PASSWORD)
    if cnxn != None: print("PROCESS DATABASE: CONNECT SUCCESS", cnxn)
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM " + TABLE_CONTROL_PLAN)
    data = cursor.fetchall()
    df = pd.DataFrame(data)
    for i in range(size):
        meta_data_natural_name = df.iloc(3, i)
        meta_data_natural_value = df.iloc(4, i)
        meta_data_natural.append(meta_data_db(meta_data_natural_name, meta_data_natural_value))
    return meta_data_natural

def parse_metadata_xml(ce_file):
    meta_temp = root_metadata()
    parsed = ET.parse(ce_file)
    root = parsed.getroot()
    size =0
    for step in root:
        try:
            meta_temp.meta_data_lake.append(meta_data_xml(step.attrib.get('name'), step[1].text))
            meta_temp.size +=1
        except:
            {}
    return meta_temp

