# -*- coding: utf-8 -*-
import json, sys, os.path
from pathlib import Path

class Write_Files:
    
    def __init__(self, sqlalchemy_class_list, query_obj_list):
        self.sqlalchemy_class_list = sqlalchemy_class_list
        self.query_obj_list = query_obj_list
        self.json_objects = self.create_json_objects()


    def create_json_objects(self):
        json_objects = []
        for query_object in self.query_obj_list:
            json_obj = []
            for row in query_object:
                data_dict = {}
                for column in row.__table__.columns:
                    data_dict[column.name] = str(getattr(row, column.name))
                json_obj.append(data_dict)
            json_objects.append(json_obj)
        return json_objects
        
        
    def write_json_to_file(self):
        #print(json.dumps(self.json_objects))
        current_working_directory = str(Path.cwd())
        json_data_directory = (current_working_directory + "\json_data\\")
        Path(json_data_directory).mkdir(parents=True, exist_ok=True)
        print(json_data_directory)

        interator_counter = 0
        for json_obj in self.json_objects:
            file_to_open = (json_data_directory + self.sqlalchemy_class_list[interator_counter] + ".json")
            f = open(file_to_open, "w")
            f.write(json.dumps(json_obj))
            f.close()
            interator_counter += 1
        return