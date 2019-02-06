import pandas as pd
import time
from sklearn.cluster import KMeans
import numpy as np

start_time = time.time()

# Reading data from csv
data_temp = pd.read_csv("temperature.csv", sep=";", header=None)
data_hum = pd.read_csv("humidity.csv", sep=";", header=None)
data_pres = pd.read_csv("pressure.csv", sep=";", header=None)

# Tsnforming to data to dataframe
df_temp = pd.DataFrame(data_temp)
df_hum = pd.DataFrame(data_hum)
df_pres = pd.DataFrame(data_pres)

# print(df_temp)

df_temp = df_temp.dropna()
df_hum = df_hum.dropna()
df_pres = df_pres.dropna()

# print(df_temp)

df_temp.to_csv("temperature_df.csv", sep=',', header=None, index=False)
df_hum.to_csv("humidity_df.csv", sep=',', header=None, index=False)
df_pres.to_csv("pressure_df.csv", sep=',', header=None, index=False)

print("Stage[DATA EXTRACTION]: %s seconds." % (time.time() - start_time))
# TODO read file
# TODO crear lista

data_temp = pd.read_csv("temperature_df.csv", sep=",")
data_hum = pd.read_csv("humidity_df.csv", sep=",")
data_pres = pd.read_csv("pressure_df.csv", sep=",")

df_temp = pd.DataFrame(data_temp)
df_hum = pd.DataFrame(data_hum)
df_pres = pd.DataFrame(data_pres)

# Resizing data set
df_temp = df_temp.drop(df_temp.columns[35], axis=1)
df_hum = df_hum.drop(df_hum.columns[35], axis=1)

values_temp = df_temp.values
values_hum = df_hum.values
values_pres = df_pres.values

list_temp = list(values_temp)
list_hum = list(values_hum)
list_pres = list(values_pres)

# Size of data set
#
# print("Data set size (%d, %d)" % (len(list_temp), len(list_temp[0])))
# print("Data set size (%d, %d)" % (len(list_hum), len(list_hum[0])))
# print("Data set size (%d, %d)" % (len(list_pres), len(list_pres[0])))

# Resizing data set

list_temp = list_temp[0:36262]
list_pres = list_pres[0:36262]

# print("Data set size (%d, %d)" % (len(list_temp), len(list_temp[0])))
# print("Data set size (%d, %d)" % (len(list_hum), len(list_hum[0])))
# print("Data set size (%d, %d)" % (len(list_pres), len(list_pres[0])))

training_list = np.array([list_temp, list_hum, list_pres], dtype=np.float)

# Preparing training data set

print("Stage[DATA TRANSFORMATION]: %s seconds." % (time.time() - start_time))
# print("Data set size (%d, %d)" % (len(training_list), len(training_list[0])))

kmeans = KMeans(n_clusters=3, random_state=0).fit(list_temp)
# print(kmeans.labels_)
# Getting the cluster centers
C = kmeans.cluster_centers_
# print(C)
print("Stage[DATA ENTRENAMIENTO ]: %s seconds." % (time.time() - start_time))

testing_data = np.random.rand(2, 35)
kmeans.predict(testing_data)

print("Stage[DATA TESTING ]: %s seconds." % (time.time() - start_time))
