from flask import Flask, render_template
import numpy as np
import matplotlib.pyplot as plt
from Cppn import Cppn

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

##@app.route('/generate',methods=['POST','GET'])
##def cppn():
#    return 

if __name__ == '__main__':
    app.run(debug=True)
    
