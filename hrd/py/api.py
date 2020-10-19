from flask import Flask,request,make_response
import json
from splitImage import getImage
from minSteps import getMethod
from rank import getRank,writedata

app = Flask(__name__)

@app.route("/getData")
def h1():
    dataMap = getImage()
    data = json.dumps(dataMap)
    rsp = make_response(data)
    rsp.headers['Access-Control-Allow-Origin'] = '*'
    return rsp

@app.route('/getPath', methods=['POST'])
def h2():
    s = request.form['pos']
    k = request.form['white']
    strr=""
    for i in s:
        if i>="0" and i<="9":
            strr+=i

    d = getMethod(strr,str(k))
    data = json.dumps(d)
    rsp = make_response(data)
    
    rsp.headers['Access-Control-Allow-Origin'] = '*'
    return rsp

@app.route("/getRank")
def h3():
    dataMap = getRank()
    data = json.dumps(dataMap)
    rsp = make_response(data)
    rsp.headers['Access-Control-Allow-Origin'] = '*'
    return rsp

@app.route("/addRank", methods=['POST'])
def h4():
    date = request.form['date']
    step = request.form['step']
    time = request.form['time']
    writedata(int(step),int(time),date)

    rsp = make_response(json.dumps({"status":"success"}))
    rsp.headers['Access-Control-Allow-Origin'] = '*'
    return rsp
    
if __name__ == '__main__':
    app.run()