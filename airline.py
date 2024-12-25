import pandas as pd 
import seaborn as s
import matplotlib.pyplot as plt

#load the data from flights.csv file
data = s.load_dataset("flights")

ove_pasger_trafic = data.groupby(['month'])['passengers'].sum()
ove_pasger_trafic.plot(figsize = (5,5))

plt.xlabel("Months")
plt.ylabel("passangers Traffic")
plt.title("Overal month passenger Traffic")

plt.show()

