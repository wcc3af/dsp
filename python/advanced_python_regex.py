# Just as a note I originally wrote the code in jupyter notebook

import pandas as pd
import numpy as np

data = pd.read_csv("faculty.csv")

data.describe()
data.head()

data.columns() # needed this to see the spaces in front of some of the columns

# Finding the degrees
data[" degree"].unique() # to establish a shorter list of what to look at

phd_pattern = r'.*Ph.*'
scd_pattern = r'.*Sc.*'
md_pattern = r'.*MD.*'
mph_pattern = r'.*MPH.*'
bsed_pattern = r'.*B.S.Ed.*'
ma_pattern = r'.*MA.*'
ms_pattern = r'.*MS.*'
jd_pattern = r'.*JD.*'

phds = data[data[" degree"].str.contains(phd_pattern)]
scds = data[data[" degree"].str.contains(scd_pattern)]
mds = data[data[" degree"].str.contains(md_pattern)]
mphs = data[data[" degree"].str.contains(mph_pattern)]
bseds = data[data[" degree"].str.contains(bsed_pattern)]
mas = data[data[" degree"].str.contains(ma_pattern)]
mss = data[data[" degree"].str.contains(ms_pattern)]
jds = data[data[" degree"].str.contains(jd_pattern)]

print("number of phds: ",phds.shape[0])
print("number of scds: ",scds.shape[0])
print("number of mds: ",mds.shape[0])
print("number of mphs: ",mphs.shape[0])
print("number of bseds: ",bseds.shape[0])
print("number of mas: ",mas.shape[0])
print("number of mss: ",mss.shape[0])
print("number of jds: ",jds.shape[0])

# Finding different titles:
data[' title'].unique()

assoc = data[data[" title"].str.contains(r'Associate')]
prof = data[data[" title"].str.contains(r'^Professor')]
assist = data[data[" title"].str.contains(r'Assistant')]

print "assoc profs: ",assoc.shape[0]
print "profs: ",prof.shape[0]
print "assistants: ",assist.shape[0]

# Putting emails in a list
emails = data[" email"].tolist()

# Finding Unique domains
reduced_emails = []
for email in emails:
    reduced_emails.append(email[email.index("@")+1:]) # removing everything before and including '@'

list(set(reduced_emails)) # make a list of the unique domains by turning the original list into a set then back into a list
