from flask import Flask, render_template, request
import pickle
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('Database/UserSavedData.db', check_same_thread=False)

pickled_model = pickle.load(open(f'ML Model/model.pkl', 'rb'))

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

    cur = conn.cursor()
    query = '''INSERT INTO saved_data (Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome) VALUES (?,?,?,?,?,?,?,?,?)'''
    
    if(result.astype(int) == 1):
        output = "Tested Positive for Diabetes"
        out = 1
    else:
        output = "Tested Negative for Diabetes"
        out = 0

    cur.execute(query,(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,Bmi,DiabetesPedigreeFunction,age,out))

    conn.commit()
    conn.close()

    return render_template("result.html",result = output)


if __name__ == '__main__':
   app.run()