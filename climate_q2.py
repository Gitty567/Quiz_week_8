import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"./climate.csv")

# Instead of appending, I added each column data to the existing list and simply just used the 'tolist()' method to
# add the corresponding data.

years = df["Year"].tolist()
co2 = df["CO2"].tolist()
temp = df["Temperature"].tolist()

# This data will be read by matplotlib and the graph will be made
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year")

plt.tight_layout()

plt.show()
