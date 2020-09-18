from flask import Flask, render_template
import numpy as np
import matplotlib.pyplot as plt
from Cppn import Cppn
import os
import time
from PIL import Image


app = Flask(__name__)

@app.route('/')
def home():
    M = Cppn()
    r = M(450,600,10)
    im = Image.fromarray(r)

    new_graph_name = "Res" + str(time.time()) + ".png"

    saveloc = 'static/Dyaimages/'

    new_graph_name = "Res" + str(time.time()) + ".png"

    for filename in os.listdir(saveloc):
        if filename.startswith('Res'):  # not to remove other images
            os.remove(saveloc + filename)
    

    im = im.save(saveloc + new_graph_name) 

    return render_template("index.html",graph= "/Dyaimages/"+new_graph_name)



if __name__ == '__main__':
    app.run(debug=True)
    
