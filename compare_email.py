import pandas as pd

# Read the first CSV file
df1 = pd.read_csv('data/file1.csv')

# Read the second CSV file
df2 = pd.read_csv('data/file2.csv')

column1_file1 = df1.iloc[:, 0]
print(len(column1_file1))
email_column_file2 = df2['email'] 
print(len(email_column_file2))
matches = column1_file1.isin(email_column_file2)

# Filter the matched rows
matched_data = df1[matches]
unmatched_data = df1[~matches]

# Save the matched data to a new CSV file
matched_data.to_csv('data/matched_file.csv', index=False)
unmatched_data.to_csv('data/unmatched_file.csv', index=False)