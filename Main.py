# Load the Pandas libraries with alias 'pd'
import pandas as pd
import numpy as np
import time
import statistics

# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
# Get starting time
start_time = time.time()

data_temp = pd.read_csv("temperature.csv")
data_hum = pd.read_csv("humidity.csv")
data_pres = pd.read_csv("pressure.csv")
print("Stage[DATA EXTRACTION]: %s seconds." % (time.time() - start_time))
# Preview the first 5 lines of the loaded data
data_temp.head()

df_temp = pd.DataFrame(data_temp)
df_hum = pd.DataFrame(data_hum)
df_pres = pd.DataFrame(data_pres)
df_classification = pd.DataFrame(columns=['Time', 'City', 'Temperature', 'Humidity', 'Pressure', 'Class'])

print("Stage[DATA TRANSFORMATION]: %s seconds." % (time.time() - start_time))

headers = list(df_temp)
del headers[0]
print(headers)
# print(df_temp)
# Size of dataframes
# print(df_temp.shape)
# print(df_hum.shape)
# print(df_pres.shape)
print("Stage[DATA CLASSIFICATION START]: %s seconds." % (time.time() - start_time))
for col in headers:
    print("CLASSIFYING " + df_temp[col])
    print("Temperature")
    mean_temp = df_temp.loc[:, col].mean()
    min_temp = df_temp.loc[:, col].min()
    max_temp = df_temp.loc[:, col].max()
    print("Mean temp ", mean_temp)
    print("Min temp ", min_temp)
    print("Max temp ", max_temp)

    print("Humidity")
    mean_hum = df_hum.loc[:, col].mean()
    min_hum = df_hum.loc[:, col].min()
    max_hum = df_hum.loc[:, col].max()
    print("Mean temp ", mean_hum)
    print("Min temp ", min_hum)
    print("Max temp ", max_hum)

    print("Pressure")
    mean_pres = df_pres.loc[:, col].mean()
    min_pres = df_pres.loc[:, col].min()
    max_pres = df_pres.loc[:, col].max()
    print("Mean temp ", mean_pres)
    print("Min temp ", min_pres)
    print("Max temp ", max_pres)

    # for index in range(0, df_temp.shape[0]):
    for index in range(0, 10):
        current_temp = df_temp[col][index]
        current_hum = df_hum[col][index]
        current_pressure = df_pres[col][index]
        new_row = {'Time': df_temp['datetime'][index], 'City': col, 'Temperature': df_temp[col][index],
                   'Humidity': df_hum[col][index],
                   'Pressure': df_pres[col][index]}
        print(new_row)
        if current_temp >= mean_temp and current_hum <= mean_hum:
            new_row['Class'] = "Soleado"
        elif current_hum > mean_hum and current_temp <= mean_temp:
            new_row['Class'] = "Lluvioso"
        #     Adding new classified object
        df_classification = df_classification.append(new_row, ignore_index=True)
    print("\nStage[CLASSIFICATION] (%s): %s seconds." % (col, time.time() - start_time))
print(df_classification)
# Print execution time
print("Stage[DATA CLASSIFICATION END]: %s seconds." % (time.time() - start_time))
