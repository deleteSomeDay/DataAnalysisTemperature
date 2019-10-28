import matplotlib.pyplot as plt
import numpy as np
import pandas as panda

airTemp = np.array(panda.read_excel("Air.xlsx"))
time = airTemp[0:24, 0]

temp = np.array(panda.read_excel("Temp.xlsx"))
temp = temp[:, 1]
print(temp)
plt.plot(temp-airTemp, time)
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Body Temperature - Air Temperature vs Time")
plt.show()
data = []