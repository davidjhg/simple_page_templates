from sys import prefix
from flask import Flask, render_template, redirect, url_for
from flask.templating import render_template_string

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask import request
# import config
import hgtk

app = Flask(__name__)

import os

import json 

    
num2result_image_path = {
    0:"",
    1:"",
    2:"",
    3:""
}

@app.route('/index',methods=("GET","POST"))
def index():
    print("index called")
    if request.method == "POST":
        submit_id = int(request.form.get("submit_id"))
        print("submit_id",submit_id)
        thr_image_path = "images/thr%d.png"%(submit_id)
        prd_image_path = "images/prd%d.png"%(submit_id)
        print(thr_image_path,prd_image_path)
        return render_template('index_prototype.html',thr_image_path=thr_image_path,prd_image_path=prd_image_path)

    elif request.method == "GET":
        return render_template('index_prototype.html')

    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)

