from flask import Flask, render_template ,Request
from flask.templating import render_template_string
from flask.wrappers import Request
import pandas as pd
import csv

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def Index():
    return render_template('index.html')

@app.route('/data',methods=['GET','POST'])
def data():
    if Request.method == 'POST':
        f = Request.form['csvfile']
        data= []
        with open(f) as file:
            csvfile = csv.reader(file)
            for row in csvfile:
                data.append(row)
        data = pd.DataFrame(data)
        return render_template('data.html', data =data.to_html(header='false',index='false'))        

if __name__=="__main__":
    app.run(debug=True)