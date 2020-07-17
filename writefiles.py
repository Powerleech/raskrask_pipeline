# -*- coding: utf-8 -*-
import json, sys, os.path
from pathlib import Path
from local_settings import FILE_PATH

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
        if FILE_PATH:
            json_data_directory = FILE_PATH
        else:
            current_working_directory = str(Path.cwd())
            json_data_directory = (current_working_directory + "/json_data/")
            
        try:
            Path(json_data_directory).mkdir(parents=True, exist_ok=True)
            #print(json_data_directory)

            interator_counter = 0
            print("Writing files to path: {} | {} files to be written".format(json_data_directory, len(self.json_objects)))
            for json_obj in self.json_objects:
                file_to_open = (json_data_directory + self.sqlalchemy_class_list[interator_counter] + ".json")
                f = open(file_to_open, "w")
                f.write(json.dumps(json_obj))
                f.close()
                interator_counter += 1
            print("Successfully wrote all files")
            return
        except:
            print("[ERROR]: Unable to write files to path: {}".format(json_data_directory))
            print("[UNEXPECTED ERROR:]", sys.exc_info())
            sys.exit()