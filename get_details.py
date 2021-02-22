import pandas as pd
import sqlite3
import os
# import fetechdata

# sqlite_file='.\SQLiteStudio-3.2.1\SQLiteStudio\Db_codique.db'
# conn = sqlite3.connect(sqlite_file)
# c = conn.cursor()

def get_project_details(project_desc):
    sqlite_file='.\SQLiteStudio-3.2.1\SQLiteStudio\Db_codique.db'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    ins_query = """INSERT INTO Project_Details (projectManager) VALUES (:desc);"""
    c.execute(ins_query, {"desc": project_desc})
    conn.commit()
    return(print('recored inserted'))