#before running run in terminal pip install pandas matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('scraped_data.csv')

# Perform some analysis
summary = data.describe()

# Save the summary to a text file
with open('summary.txt', 'w') as file:
    file.write(summary.to_string())

# Plot a histogram of a specific column
data['column_name'].hist()
plt.title('Histogram of Column Name')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.savefig('histogram.png')

print("Data analysis completed and histogram saved.")
