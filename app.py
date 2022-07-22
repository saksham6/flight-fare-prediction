import numpy as np
import pandas as pd
from flask import Flask, request,render_template
import pickle
import datetime

app= Flask(__name__ , static_url_path='/static' )


@app.route('/')
def home():
    return render_template('home.html')

# prediction function 
def ValuePredictor(to_predict_list): 
    to_predict = np.array(to_predict_list).reshape(1, 30) 
    loaded_model = pickle.load(open("fight_fare.pkl", "rb")) 
    result = loaded_model.predict(to_predict) 
    return result[0] 
  
@app.route('/result', methods = ['POST']) 
def result(): 
    if request.method == 'POST': 
        to_predict_list = request.form.to_dict() 
        to_predict_list = list(to_predict_list.values()) 
        to_predict_date_list = int(datetime.datetime.utcnow().timestamp())
        to_predict_list = list(map(int, [to_predict_date_list,to_predict_list])) 
        result = ValuePredictor(to_predict_list)         
                    
        return render_template("result.html", prediction = result) 
        


if __name__ == "__main__":
    app.run(debug=True, port= 5000)
    #app.run(host='0.0.0.0', port =5000)