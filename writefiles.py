# -*- coding: utf-8 -*-
import json, sys, csv
from pathlib import Path
from local_settings import FILE_PATH
from local_settings import CSV_OR_JSON

class Write_Files:
    
    def __init__(self, sqlalchemy_class_list, query_obj_list):
        self.file_path = FILE_PATH
        self.sqlalchemy_class_list = sqlalchemy_class_list
        self.query_obj_list = query_obj_list
        self.objects_list = self.create_object_list()


    def create_object_list(self):
        objects_list = []
        for query_object in self.query_obj_list:
            obj = []
            for row in query_object:
                data_dict = {}
                for column in row.__table__.columns:
                    data_dict[column.name] = str(getattr(row, column.name))
                obj.append(data_dict)
            objects_list.append(obj)
        return objects_list

        
    def write_files(self):
        if self.file_path:
            data_directory = self.file_path
        else:
            current_working_directory = str(Path.cwd())
            data_directory = (current_working_directory + "/data/")
            
        try:
            Path(data_directory).mkdir(parents=True, exist_ok=True)
            interator_counter = 0
            print("Writing {} files to path: {} | {} files to be written".format(CSV_OR_JSON, data_directory, len(self.objects_list)))
            if CSV_OR_JSON == "json":
                self.write_json(interator_counter, data_directory)
            elif CSV_OR_JSON == "csv":
                self.write_csv(interator_counter, data_directory)
            else:
                print("[ERROR]: invalid value set in 'CSV_OR_JSON', value is: {}, value can be 'json' or 'csv'".format(CSV_OR_JSON))
                sys.exit()

            print("Successfully wrote all files")

        except:
            print("[ERROR]: Unable to write files to path: {}".format(data_directory))
            print("[UNEXPECTED ERROR:]", sys.exc_info())
            sys.exit()
        
    def write_json(self, interator_counter, data_directory):
        for json_obj in self.objects_list:
            file_to_open = (data_directory + self.sqlalchemy_class_list[interator_counter] + ".json")
            f = open(file_to_open, "w")
            f.write(json.dumps(json_obj))
            f.close()
            interator_counter += 1

        
    def write_csv(self, interator_counter, data_directory):
        for csv_obj in self.objects_list:
            file_to_open = (data_directory + self.sqlalchemy_class_list[interator_counter] + ".csv")
            f = open(file_to_open, "w")
            writer = csv.DictWriter(f, fieldnames=list(csv_obj[0].keys()))
            writer.writeheader()
            writer.writerows(csv_obj)
            f.close()
            interator_counter += 1