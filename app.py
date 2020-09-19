from flask import Flask, render_template,request
import numpy as np
import matplotlib.pyplot as plt
from Cppn import Cppn
import os
import time
from PIL import Image


app = Flask(__name__)
M = Cppn()

@app.route('/')
def home(h=450,w=600,z=10):
    r = M(h,w,z)
    
    im = Image.fromarray(r)

    new_graph_name = "Res" + str(time.time()) + ".png"

    saveloc = 'static/Dyaimages/'

    new_graph_name = "Res" + str(time.time()) + ".png"

    for filename in os.listdir(saveloc):
        if filename.startswith('Res'):  # not to remove other images
            os.remove(saveloc + filename)
    
    im = im.save(saveloc + new_graph_name) 

    return render_template("index.html",graph= "/Dyaimages/"+new_graph_name)

@app.route('/gen',methods = ['POST', 'GET'])
def update():
    print(request.form)
    print(request.values)
    print(request.args.get("name1"))
    return home(450,600,5)

if __name__ == '__main__':
    app.run(debug=True)
    
