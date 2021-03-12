import pandas as pd
import sqlite3
import os
from get_details import *
from flask import Flask, request, render_template,url_for,send_file,redirect

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def fetechdata():
    if request.method == 'POST':
        mname = request.form['managername']
        pname = request.form['projectname']
        nors = request.form['prjdesc']
        
        get_project_details(mname,pname,nors)
        displayOP = display()
       
            
        return render_template('dashboard.html',mname=mname,pname=pname,nors=nors,displayOP=displayOP)
    elif request.method == 'GET':
        return render_template('dashboard.html')
        
        
if __name__ == "__main__":
    app.run(debug=True)
    
    
    