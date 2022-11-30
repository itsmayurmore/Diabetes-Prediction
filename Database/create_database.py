import sqlite3

conn = sqlite3.connect('UserSavedData.db')


conn.execute('''CREATE TABLE saved_data
         (Pregnancies INT ,
         Glucose       REAL,
         BloodPressure            REAL,
         SkinThickness        REAL,
         Insulin         REAL,
         BMI REAL,
         DiabetesPedigreeFunction   REAL,
         Age INT,
         Outcome  INT);''')

conn.close()