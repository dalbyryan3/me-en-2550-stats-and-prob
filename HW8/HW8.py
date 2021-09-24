# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 19:49:07 2019
ME EN 2550
Homework 8
@author: Ryan Dalby
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

#B1
print("B1")
b1data = pd.DataFrame({"viscosity": [0.45, 0.20, 0.34, 0.58, 0.70, 0.57, 0.55, 0.44], "ratio":[1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3]})
plt.scatter(b1data['ratio'], b1data['viscosity'])
print("b)")
b1model = sm.OLS.from_formula(formula="viscosity ~ np.power(ratio,2)", data=b1data).fit()
b1predictions = b1model.predict(b1data['ratio'])
plt.plot(b1data['ratio'], b1predictions)
plt.show()
print("a)")
print(b1model.summary())
print()

#B2
print("\n\nB2")
age = [55,46,30,35,59,61,74,38,27,51,53,41,37,24,42,50,58,60,62,68,70,79,63,39,49]
severity = [50,24,46,48,58,60,65,42,42,50,38,30,31,34,30,48,61,71,62,38,41,66,31,42,40]
surg = [0,1,1,1,0,0,1,1,0,1,1,0,0,0,0,1,1,1,0,0,1,1,1,0,1]
anx = [2.1,2.8,3.3,4.5,2.0,5.1,5.5,3.2,3.1,2.4,2.2,2.1,1.9,3.1,3.0,4.2,4.6,5.3,7.2,7.8,7.0,6.2,4.1,3.5,2.1]
sat = [68,77,96,80,43,44,26,88,75,57,56,88,88,102,88,70,52,43,46,56,59,26,52,83,75]
b2data = pd.DataFrame({"age": age, "severity":severity, "surgmed":surg, "anxiety":anx, "satisfaction":sat})
b2model = sm.OLS.from_formula(formula="satisfaction ~ age + severity + surgmed + anxiety", data=b2data).fit()
print("a)")
print(b2model.summary())
print("b)")
print("Standard error of regression coefficents: \n{}".format(b2model.bse))
print("c) Not all the model parameters are estimated with the same precision.  This is because all parameters are fit to a single model and thus the predictors will have varying standard error values/precision")


#B3
print("\n\nB3")
y = [240,236,270,274,301,316,300,296,267,276,288,261]
x1 = [25,31,45,60,65,72,80,84,75,60,50,38]
x2 = [24,21,24,25,25,26,25,25,24,25,25,23]
x3 = [91,90,88,87,91,94,87,86,88,91,90,89]
x4 = [100,95,110,88,94,99,97,96,110,105,100,98]
b3data = pd.DataFrame({"y":y,"x1":x1,"x2":x2,"x3":x3,"x4":x4})
b3model = sm.OLS.from_formula(formula="y ~ x1 + x2 + x3 + x4", data=b3data).fit()
print("a)")
print(b3model.summary())
print("b)")
print("Standard error of regression coefficents: \n{}".format(b3model.bse))
print("Not all the model parameters are estimated with the same precision.  This is because all parameters are fit to a single model and thus the predictors will have varying standard error values/precision")
print("c)")
b3predict = b3model.predict(exog = dict(x1 = 75, x2 = 24, x3 = 90, x4 = 98))
print("The predicted power consumption for a month with the given values is : {}\n\n\n\n\n\n".format(str(b3predict)[5:-1]))
