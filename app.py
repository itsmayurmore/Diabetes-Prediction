from flask import Flask, render_template, request
import pickle
import mysql.connector
import os
app = Flask(__name__)

mydb = mysql.connector.connect(
  host=os.getenv('HOST'),
  user=os.getenv('USER'),
  password=os.getenv('PASSWORD'),
  database=os.getenv('DATABASE')
)
mycursor = mydb.cursor()

pickled_model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def student():
   return render_template('index.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
    age = request.form.get('age')
    Pregnancies = request.form.get('Pregnancies')
    Glucose = request.form.get('Glucose')
    BloodPressure = request.form.get('BloodPressure')
    SkinThickness = request.form.get('SkinThickness')
    Insulin = request.form.get('Insulin')
    Bmi = request.form.get('BMI')
    DiabetesPedigreeFunction = request.form.get('DiabetesPedigreeFunction')
    l = [Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,Bmi,DiabetesPedigreeFunction,age]
    result = pickled_model.predict([l])

    query = '''INSERT INTO Diabetes_data (Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
    
    if(result.astype(int) == 1):
        output = "Tested Positive for Diabetes"
        out = 1
    else:
        output = "Tested Negative for Diabetes"
        out = 0

    values = (Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,Bmi,DiabetesPedigreeFunction,age,out)
    mycursor.execute(query,values)

    mydb.commit()

    return render_template("result.html",result = output)


if __name__ == '__main__':
   app.run(debug=True)