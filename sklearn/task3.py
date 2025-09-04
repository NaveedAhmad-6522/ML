# Features (X)
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
study_hours = [2.5, 3.0, 4.5, 5.0, 6.0, 1.5, 3.5]
attendance =  [60,  70,  85,  90,  95,  40,  80]
prev_scores = [55,  60,  75,  80,  88,  45,  70]
y = [58, 65, 78, 84, 92, 48, 74]
a=np.array(study_hours)
b=np.array(attendance)
c=np.array(prev_scores)
X=np.stack((a,b,c),axis=1)
X1=np.column_stack((a,b,c))
a=np.array(study_hours).reshape(-1,1)
b=np.array(attendance).reshape(-1,1)
c=np.array(prev_scores).reshape(-1,1)
np.concatenate((a,b,c),axis=1)

regressor=LinearRegression()
regressor.fit(X,y)

plt.scatter(study_hours, y, label='Actual')
plt.plot(study_hours, regressor.predict(X), label='Predicted', color='red')

plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.title("Score Prediction based on Study Hours + Attendance + Previous Score")
plt.legend()
plt.grid(True)
plt.show()