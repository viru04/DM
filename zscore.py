import pandas as pd

# Load the CSV file
data = pd.read_csv('Sales_Transactions.csv')  # Adjust the file path if necessary

# Select the columns that need normalization
columns_to_normalize = [f'W{i}' for i in range(52)]  # Assuming W0 to W51 columns
data_to_normalize = data[columns_to_normalize]

# Apply Z-score normalization using the formula: Z = (X - mean) / std
zscore_normalized_data = (data_to_normalize - data_to_normalize.mean()) / data_to_normalize.std()

# Add the 'Product_Code' back to the normalized data
zscore_normalized_data['Product_Code'] = data['Product_Code']

# Save the Z-score normalized data to a new CSV file
zscore_normalized_data.to_csv('Zscore_Normalized_Sales_Transactions.csv', index=False)

print("Z-score normalization complete using manual formula. Data saved to 'Zscore_Normalized_Sales_Transactions.csv'")
