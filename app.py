import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('pickle.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')
   

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        
        Item_Weight=float(request.form["Item_Weight"])
        Item_Fat_Content=int(request.form["Item_Fat_Content"])
        Item_Visibility=float(request.form["Item_Visibility"])
        Item_Type=int(request.form["Item_Type"])
        Item_MRP=float(request.form["Item_MRP"])
        Outlet_Establishment_Year=int(request.form["Outlet_Establishment_Year"])
        Outlet_Size=int(request.form["Outlet_Size"])
        Outlet_Location_Type=int(request.form["Outlet_Location_Type"])
        Outlet_Type=int(request.form['Outlet_Type'])

        
        
        data = np.array([[Item_Weight,Item_Fat_Content,Item_Visibility,Item_Type,Item_MRP,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Outlet_Type]])
        my_prediction = model.predict(data)
        
        return render_template('home.html', prediction=my_prediction)

        
if __name__ == '__main__':
    app.run()