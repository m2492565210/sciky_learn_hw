'''
Created on 2018年10月13日

@author: emti
'''
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

loaded_data = datasets.load_boston()
data_X = loaded_data.data
data_y = loaded_data.target
 
model = LinearRegression()
model.fit(data_X, data_y)
 
print(model.predict(data_X[:4, :]))
print(data_y[:4])

print(model.coef_)
print(model.intercept_)
print(model.get_params())
print(model.score(data_X, data_y))