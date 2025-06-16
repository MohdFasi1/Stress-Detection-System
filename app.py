import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

stress = pickle.load(open('model/stress_model.pkl','rb'))

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')
 

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
	return render_template('login.html')


@app.route('/teststress', methods = ['GET', 'POST'])
def teststress():
    return render_template('prediction.html')

@app.route('/performance')
def performance():
    return render_template('performance.html')


@app.route('/predict',methods=['POST'])
def predict():
	int_feature = [x for x in request.form.values()]
	 
	final_features = [np.array(int_feature)]
	 
	result=stress.predict(final_features)
	if result == 0:
		result = "Low/Normal"
	elif  result == 1:
		result = "Medium Low"
	elif result == 2:
		result = "Medium"
	elif result == 3:
		result = "Medium High"
	elif result == 4:
		result = "High"			
	else:
		result = ""
	return render_template('prediction.html', prediction_text= 'Stress Level: {}'.format(result))
    
    
    
if __name__ == "__main__":
    from os import environ
    port = int(environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

