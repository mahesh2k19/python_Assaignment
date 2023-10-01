import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a data frame
df = pd.read_csv('data.csv')

# Select the columns that you want to plot
x = df['x']
y = df['y']

# Create a plot
plt.plot(x, y)

# Customize the plot
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Line Graph')

# Display the plot
plt.show()
