# -- coding: utf-8 --
import sys
from local_settings import SQLALCHEMY_DATABASE_URI
#from datatransform import Data_Transform
#from preprocessor import Preprocessor
from writefiles import Write_Files

import sqlalchemy
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session


class Interface:
    def __init__(self):
        self.engine, self.engine_base, self.engine_session, self.sqlalchemy_class_list = self.establish_database_connection()


    def establish_database_connection(self):
        try:
            #engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
            engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI)
            base = automap_base()
            base.prepare(engine, reflect=True) #SHOW CREATE TABLE...
            session = Session(engine)
            sqlalchemy_class_list = [a for a in dir(base.classes) if not a.startswith('__')]
            return engine, base, session, sqlalchemy_class_list
        
        except:
            print("[ERROR]: Unable to establish connection to database")
            print("[UNEXPECTED ERROR:]", sys.exc_info())
            sys.exit()

# DEBUGGING / INFO ------------------------------------------------------------


    def database_metadata(self):
        if self.engine_base == None or self.engine_session == None:
            print("[ERROR]: No engine object to perform queries on")
            sys.exit()
        else:
            print("Printing database metadata: \n")

            for class_obj in self.sqlalchemy_class_list:
                class_object_count = eval("self.engine_session.query(self.engine_base.classes.{}).count()".format(class_obj))
                class_object_first = eval("self.engine_session.query(self.engine_base.classes.{}).first()".format(class_obj))
                print("class table: " + class_obj + " - number of rows: " + str(class_object_count))
                field_list = class_object_first.__table__.columns
                for field in field_list:
                    str_field = str(field)
                    print("table field: {} | class variable: {}".format(str_field.split('.')[-1], field))
                print("\n")
                
# DEBUGGING / INFO ------------------------------------------------------------

            
    def create_query_obj_limited(self, query_obj_list):
        if self.engine_base == None or self.engine_session == None:
            print("[ERROR]: No engine object to perform queries on")
            sys.exit()
        else:
            for class_obj in self.sqlalchemy_class_list:
                query_object = eval("self.engine_session.query(self.engine_base.classes.{}).limit(2).all()".format(class_obj))
                query_obj_list.append(query_object)
            return query_obj_list


    def get_sqlalchemy_class_list(self):
        return self.sqlalchemy_class_list


if __name__ == "__main__":
    interface = Interface()
    interface.database_metadata()
    query_obj_list = []
    query_obj_list = interface.create_query_obj_limited(query_obj_list)
    sqlalchemy_class_list = interface.get_sqlalchemy_class_list()
    
    file_writer = Write_Files(sqlalchemy_class_list, query_obj_list)
    file_writer.write_json_to_file()
