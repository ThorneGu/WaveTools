import glob
import pandas as pd
import numpy as np
import csv
import os

dirs = os.listdir(path="/VIBDATASET/original data")
print(dirs)

for dir in dirs:
    txt_files = []
    path = "/VIBDATASET/original data/" + dir
    names = os.listdir(path)
    for file in names:
        file_name = os.path.join(path, file)
        txt_files.append(file_name)

    for file in txt_files:
        data_list = []
        time_data_list = []
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
            filename = "/VIBDATASET/wavedata/" + dir + "/" + time + ".csv"
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
                writer.writerow(["data"])
                for row in data:
                    writer.writerow([row])
