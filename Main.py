# Load the Pandas libraries with alias 'pd'
import pandas as pd
import numpy as np
import time
import statistics

# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
data_temp = pd.read_csv("temperature.csv")
data_hum = pd.read_csv("humidity.csv")
data_pres = pd.read_csv("pressure.csv")
# Preview the first 5 lines of the loaded data
data_temp.head()

# Get starting time
start_time = time.time()

df_temp = pd.DataFrame(data_temp)
df_hum = pd.DataFrame(data_hum)
df_pres = pd.DataFrame(data_pres)
df_classification = pd.DataFrame(columns=['Time', 'Temperature', 'Humidity', 'Pressure', 'Class'])

headers_temp = list(df_temp)
# print(df_temp)
print(headers_temp)

print(df_temp.shape)
print(df_hum.shape)
print(df_pres.shape)

print("Temperature")
mean_temp = df_temp.loc[:, "Vancouver"].mean()
min_temp = df_temp.loc[:, "Vancouver"].min()
max_temp = df_temp.loc[:, "Vancouver"].max()
print("Mean temp ", mean_temp)
print("Min temp ", min_temp)
print("Max temp ", max_temp)

print("Humidity")
mean_hum = df_hum.loc[:, "Vancouver"].mean()
min_hum = df_hum.loc[:, "Vancouver"].min()
max_hum = df_hum.loc[:, "Vancouver"].max()
print("Mean temp ", mean_hum)
print("Min temp ", min_hum)
print("Max temp ", max_hum)

print("Pressure")
mean_pres = df_pres.loc[:, "Vancouver"].mean()
min_pres = df_pres.loc[:, "Vancouver"].min()
max_pres = df_pres.loc[:, "Vancouver"].max()
print("Mean temp ", mean_pres)
print("Min temp ", min_pres)
print("Max temp ", max_pres)

for index in range(0, df_temp.shape[0]):
# for index in range(0, 10):
    current_temp = df_temp['Vancouver'][index]
    current_hum = df_hum['Vancouver'][index]
    current_pressure = df_pres['Vancouver'][index]
    new_row = {'Time': df_temp['datetime'][index], 'Temperature': df_temp['Vancouver'][index],
               'Humidity': df_hum['Vancouver'][index],
               'Pressure': df_pres['Vancouver'][index]}
    print(new_row)
    if current_temp >= mean_temp:
        new_row['Class'] = "Soleado"
    elif current_hum <= mean_hum:
        new_row['Class'] = "Lluvioso"
    #     Adding new classified object
    df_classification = df_classification.append(new_row, ignore_index=True)
print(df_classification)
# Print execution time
print("--- %s seconds ---" % (time.time() - start_time))
