import pandas as pd
# CSV File is input
dataFrame = pd.read_csv("C:\\A.HOMER\\Projekts\\ICT-CS Projects\\Data Science + Gen AI\\Scout One ZM\\data\\FinalStats.csv")
# Replace 'Column1', 'Column2', 'Column3' with the column names you want to select
selected_columns = dataFrame[['Column1', 'Column2', 'Column3']]
# Compute ranks for each selected column
ranked_columns = selected_columns.rank(method='average', ascending=False)
# Print the data
print("Our DataFrame...",dataFrame)