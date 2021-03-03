import json
import os

from flask import Flask, render_template, request
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

from pymongo import MongoClient

iris = load_iris()
X = iris.data
Y = iris.target

classes = ["Setosa", "Versicolour", "Virginica"]

knn=KNeighborsClassifier(n_neighbors=6)
knn.fit(X,Y)

app = Flask(__name__)

client = MongoClient(host="mongodb.default.svc.cluster.local", port=27017)

db = client["iris_data"]
results = db["results"]

@app.route("/", methods=["GET"])
def home():
    return render_template("interface.html")

@app.route("/", methods=["POST"])
def predict():
    try:
        dimensions = [float(el) for el in list(request.form.to_dict().values())]
        res = classes[int(knn.predict([dimensions]))]
        results.insert_one({
            "ip":request.remote_addr,
            "inputs":[str(dim) for dim in dimensions],
            "results":res,
            })
        return res
    except Exception as e:
        return "Error:" + e
        
if __name__ == "__main__":
    app.run(debug=True, host= '0.0.0.0')
