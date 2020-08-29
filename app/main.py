import flask
from flask import request
from flask import jsonify
from datetime import datetime
from math import ceil

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return {"name":"Nyasha"}

@app.route('/calc', methods=['POST'])
def calcSaveAmountPerMonth():
  
  savings = request.json['savings']
  plannedPurchaseDate = request.json['plannedPurchaseDate']
  startDate = request.json['startDate']
  cost = request.json['cost']

  newCost = cost - savings
  num_months = 0
  if newCost > 0:
    plannedPurchaseDate = datetime.strptime(str(plannedPurchaseDate), '%Y%m%d')
    startDate = datetime.strptime(str(startDate), '%Y%m%d')
    num_months = (plannedPurchaseDate.year - startDate.year) * 12 + (plannedPurchaseDate.month - startDate.month)
    savePerMonth = ceil((newCost/num_months)*100)/100
    return {"savePerMonth": savePerMonth, "savingPeriod": num_months}
    pass
  
  return {"savePerMonth": 0, "savingPeriod": num_months}

  
if __name__ == "__main__": 
  app.run() 