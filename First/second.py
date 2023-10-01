
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a data frame
df = pd.read_csv('data1.csv')

# Select the columns that you want to plot
x = df['country']
y = df['population']

# Create a bar plot
plt.bar(x, y)

# Customize the plot
plt.xlabel('Country')
plt.ylabel('Population (millions)')
plt.title('Population by Country')

# Display the plot
plt.show()
