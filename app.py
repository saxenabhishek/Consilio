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

    new_graph_name = "graph" + str(time.time()) + ".png"

    for filename in os.listdir('static/'):
        if filename.startswith('graph'):  # not to remove other images
            os.remove('static/' + filename)
    

    im = im.save('static/' + new_graph_name) 

    return render_template("index.html",graph=new_graph_name)



if __name__ == '__main__':
    app.run(debug=True)
    
