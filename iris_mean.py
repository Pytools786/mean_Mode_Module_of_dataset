import pandas as pd

data = pd.read_csv("iris222222.csv")


sum_data = data["SepalLengthCm"].sum()
mean_data = data["SepalLengthCm"].mean()
median_data = data["SepalLengthCm"].median()
 
print("Sum:",sum_data, "\nMean:", mean_data, "\nMedian:",median_data)
