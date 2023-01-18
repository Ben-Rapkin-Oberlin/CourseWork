# app.py
from flask import Flask, request, jsonify
from flask import Flask, render_template
import pandas as pd
import json
import plotly.express as px
import plotly
app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]



@app.get("/")
def get_countries():
    print("get")
    return jsonify(countries)


@app.post("/") #add
#@app.route('/', methods=["POST"])
def post_country():
    #print('1')
    if request.is_json:
        a=request.get_json()
       # print("here")
        countries.append(a)
        return a, 201
    return {"error": "Request must be JSON"}, 415

@app.put("/") #update
def put_country():
    if request.is_json:
        a=request.get_json()
        #print(a)
        countries[a["id"]-1]=a
        return a, 201
    return {"error": "Request must be JSON"}, 415

@app.delete("/")
def delete_country():
    if request.is_json:
        a=request.get_json()
        #print(a)
        #print(a["id"])
        #print(len(countries))
        countries.pop(a["id"]-1)

        return a, 201
    return {"error": "Request must be JSON"}, 415



@app.route('/')
def home():
    return render_template("home.html", countries=jsonify(countries))


@app.route('/results')
def lineplot():
    df = pd.read_csv('NVDA_SOXX_BTC.csv')
    fig = px.line(df, x='Date', y=['Truth','Prediction'], title='Gradient Boosted Tree')
    fig.add_vline(x=df.iloc[1832,0], line_width=3, line_dash="dash", line_color="black")
    fig.update_xaxes(rangeslider_visible=True)
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    df = pd.read_csv('NVDA_SOXX_BTCnn2.csv')
    fig = px.line(df, x='Date', y=['Truth','Prediction'], title='Neural Network')
    fig.add_vline(x=df.iloc[1832,0], line_width=3, line_dash="dash", line_color="black")
    fig.update_xaxes(rangeslider_visible=True)
    graphJSON2 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    

    df=pd.DataFrame({'Algorithm': ['GBT', 'NN'], 'Mean Squared Error' : [.000185,.000418]})
    fig = px.bar(df, x='Algorithm', y='Mean Squared Error', title='Comparative Accuracy', color='Algorithm')
    graphJSON3 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('lineplot.html', graphJSON1=graphJSON1, graphJSON2=graphJSON2, graphJSON3=graphJSON3)
