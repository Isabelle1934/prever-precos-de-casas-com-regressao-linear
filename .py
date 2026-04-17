import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load data from CSV file
data = pd.read_csv('home_dataset.csv')
 
# Extract features and target variable
house_sizes = data ['HouseSize'].values
house_prices = data['HousePrice'].values

# Visualize the data
plt.scatter(house_sizes, house_prices, marker ='o', color ='blue')
plt.title('House Prices vs. House Size')
plt.xlabel('House Size (sq.ft)')
plt.ylabel('House Price ($)')
plt.show()
