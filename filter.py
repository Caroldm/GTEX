import pandas
import csv
import numpy as np

df = pandas.read_csv("/Users/Carol/Desktop/GTEX_final/Muscle/RNAseq_young_and_old.csv")

#masked = df.mask(df!=0)
#masked.count(axis=1).div(float(len(df.columns))) > 0.05
#cleaned = df[df.mask(df==0).count(axis=1).div(float(len(df.columns))).mul(100)>95]

cleaned = df[df.mask(df!=0).count(axis=1).div(float(len(df.columns))) < 0.05]
print (cleaned)


with open("/Users/Carol/Desktop/cleaned.csv", "w") as output:
	output.write(str(cleaned))

