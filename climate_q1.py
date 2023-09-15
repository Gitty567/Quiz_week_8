import matplotlib.pyplot as plt
import sqlite3
# here are the lists
years = []
co2 = []
temp = []

# this allows the database climate.db to connect with this python file
connection = sqlite3.connect("climate.db")
cursor = connection.cursor()

# this allows the sqlite command to be used so that all the info within these 3 columns are all taken togther hence
# the 'fetchall'
cursor.execute("SELECT Year, CO2, Temperature FROM ClimateData")
row = cursor.fetchall()

# This loop allows the values to be separated which can then be added to the already defined lists through the append
# function
for r in row:
    year, co2_Num, temp_Num = r
    years.append(year)
    co2.append(co2_Num)
    temp.append(temp_Num)

# then I cna close the cursor and connection functions. Now that this is done, the matplotlib can do its job in
# generating the graphs
cursor.close()
connection.close()

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")

plt.savefig("co2_temp_1.png")

plt.show()
