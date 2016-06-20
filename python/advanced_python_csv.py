import pandas as pd
import numpy as np

data = pd.read_csv("faculty.csv")

data[" email"].to_csv("emails.csv",index=False)
