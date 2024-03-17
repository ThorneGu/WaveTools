import glob
import pandas as pd
import numpy as np
import csv

txt_files = glob.glob("F:/VIBDATASET/original data/HS1/data_2023_12_13_05_30_41.txt")
print(txt_files)

data_list = []
time_data_list = []

for file in txt_files:
    with open(file, "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            line = lines[i]
            if line.startswith("num_t"):
                time_data = line.split("=")[1].strip()
                time_data_list.append(time_data)
            if line.startswith("num_i"):
                value_data = line.split("=")[1].strip()[1:-1].split(",")
                value_data.pop()
                value_data = [int(v) for v in value_data]
                data_list.append(value_data)


data_list = np.array(data_list)        
print(np.shape(data_list))
print(len(time_data_list))

file_names = []
for time in time_data_list:
    time = time.replace(":","_")
    filename = "C:/Users/dell/Desktop/HSB1/12.13/" + time + ".csv"
    file_names.append(filename)

for name in file_names:
    name = name.replace(":","_")


data_list[data_list >= 524288] = 1048575 - data_list[data_list >= 524288]
data_list = (data_list/524287) * 4.07


for i in range(len(file_names)):
    file_name = file_names[i]
    data = data_list[i]

    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Data"])
        for row in data:
            writer.writerow([row])