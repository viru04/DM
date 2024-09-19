import pandas as pd

# Load the CSV file
data = pd.read_csv('Sales_Transactions.csv')  # Adjust the file path if necessary

# Select the columns that need normalization
columns_to_normalize = [f'W{i}' for i in range(52)]  # Assuming W0 to W51 columns
data_to_normalize = data[columns_to_normalize]

# Apply Min-Max normalization using the formula: X_norm = (X - X_min) / (X_max - X_min)
min_vals = data_to_normalize.min()
max_vals = data_to_normalize.max()
minmax_normalized_data = ((data_to_normalize - min_vals) / (max_vals - min_vals))+min_vals

# Add the 'Product_Code' back to the normalized data
minmax_normalized_data['Product_Code'] = data['Product_Code']

# Save the Min-Max normalized data to a new CSV file
minmax_normalized_data.to_csv('MinMax_Normalized_Sales_Transactions.csv', index=False)

print("Min-Max normalization complete using manual formula. Data saved to 'MinMax_Normalized_Sales_Transactions.csv'")
