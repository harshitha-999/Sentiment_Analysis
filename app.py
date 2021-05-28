
from flask import Flask, render_template, request
import pickle
import sys
from sklearn.linear_model import LogisticRegression
 
app = Flask(__name__)
 
 
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/predict',methods=['POST'])
def predict():
 
    if request.method == 'POST':
 
        desc = request.form['desc']
       
 
        data =[desc]
        
 
        lr = pickle.load(open('senti.pkl', 'rb'))
        prediction = lr.predict(data)
        #sad U+1F641	
        # happy U+1F603	
        if(prediction [0] == 'happy'):
            prediction = " Positive " + '\U0001F603'
        if(prediction [0] == 'not happy'):
            prediction = "Negative " + '\U0001F641'    
       
 
    return render_template('index.html', prediction= prediction)
    #return "Hello"
 
 
 
if __name__ == '__main__':
    app.run(debug=True)     
