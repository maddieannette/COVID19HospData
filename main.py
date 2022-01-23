import pandas as pd
import numpy as np

covidData = pd.read_csv(r'covid-hospitalizations.csv')
print(covidData.head(20))