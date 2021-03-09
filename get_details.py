import pandas as pd
import sqlite3
import os
# import fetechdata

# sqlite_file='.\SQLiteStudio-3.2.1\SQLiteStudio\Db_codique.db'
# conn = sqlite3.connect(sqlite_file)
# c = conn.cursor()

def get_project_details(project_pname,project_mname,project_resource):
    sqlite_file='.\SQLiteStudio-3.2.1\SQLiteStudio\Db_codique.db'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    ins_query = """INSERT INTO Project_Details (projectManager,projectName,NumOfResources) VALUES (:mname,:pname,:nors);"""
    c.execute(ins_query, {"mname": project_pname,"pname":project_mname,"nors":project_resource})
    conn.commit()
    return(print('recored inserted'))