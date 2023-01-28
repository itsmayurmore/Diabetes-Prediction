
# Diabetes Prediction

Diabetes is a chronic condition characterized by high levels of sugar (glucose) in the blood. It is caused by a combination of factors, including genetics, lifestyle, and environmental factors. Diabetes can have serious complications if left untreated, including heart disease, nerve damage, blindness, and kidney damage.

A diabetes prediction model using logistic regression is a machine learning algorithm that can predict the likelihood of an individual having diabetes based on certain input variables. These input variables, also known as features, can include age, body mass index (BMI), number of pregnancies, insulin levels, skin thickness, blood pressure, glucose levels, and diabetes pedigree function (DPF). The DPF is a measure of the risk of diabetes based on family history and genetic factors.

The output of the model is a binary classification, meaning it will predict either "have diabetes" or "do not have diabetes." The model will use the input variables to make this prediction by fitting a curve to the data and determining the probability of an individual having diabetes based on their feature values.

To create a diabetes prediction model using logistic regression, a dataset with a large number of examples (patients) is needed. Each example should include the input variables (age, BMI, etc.) as well as the output variable (have diabetes or not). The model will then be trained on this data, using an optimization algorithm to find the best fit curve. Once the model is trained, it can be used to make predictions on new data (patients) by inputting the relevant feature values and using the curve to calculate the probability of the individual having diabetes.



## Demo

https://diabetespredict.pythonanywhere.com/


## Run Locally

Clone the project

```bash
  git clone https://github.com/itsmayurmore/Diabetes-Prediction.git
```


Install dependencies
```bash
  Install Python 3.x
```

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python app.py
```

