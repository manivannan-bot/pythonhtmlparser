
# prompt: sum these values using for loop praveeen

# prompt: sum these values using for loop manivannan


import pandas as pd

# Get the path to the file.
filepath = 'sample_data/california_housing_test.csv'


df = pd.read_csv(filepath)

sum_median_house_value = 0
for value in df['median_house_value']:
  if(value>=100000): 
     sum_median_house_value += value


print(sum_median_house_value)mani1111