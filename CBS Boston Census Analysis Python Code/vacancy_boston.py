# import module
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read dataset
boston_dfs = [pd.read_csv("./data/" + "boston" + "/ACSDT1Y" + str(year) + ".B25002_data_with_overlays_2021-10-18T223715.csv") for year in range(2010, 2020)]

occupied_ma = []
occupied_boston = []
vacant_ma = []
vacant_boston = []

for df in boston_dfs:
    occupied_ma.append(int(df['B25002_002E'][1]))
    occupied_boston.append(int(df['B25002_002E'][2]))
    vacant_ma.append(int(df['B25002_003E'][1]))
    vacant_boston.append(int(df['B25002_003E'][2]))

print("vacant  : ", vacant_boston)
print("occupied: ", occupied_boston)

# compute the rate of change over the years
roc_vacant_boston = np.diff(vacant_boston) / vacant_boston[:-1]
roc_occupied_boston = np.diff(occupied_boston) / occupied_boston[:-1]

data = [vacant_boston, occupied_boston]

columns = ('2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019')
rows = ['occupied', 'vacant']

# Get some pastel shades for the colors
# colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
colors = ['#f9bc86', '#b5ffb9']
n_rows = len(data)

index = np.arange(len(columns)) + 0.3
bar_width = 0.4

# Initialize the vertical-offset for the stacked bar chart.
y_offset = np.zeros(len(columns))

# Plot bars and create text labels for the table
cell_text = []
for row in range(n_rows):
    plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
    y_offset = y_offset + data[row]
    cell_text.append([int(x) for x in y_offset])
# Reverse colors and text labels to display the last value at the top.
colors = colors[::-1]
cell_text.reverse()

# Add a table at the bottom of the axes
the_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom')

# Adjust layout to make room for the table:
plt.subplots_adjust(left=0.2, bottom=0.2)

plt.xticks([])
plt.title('Vacant/Occupied in Boston')

plt.show()


plt.plot(roc_occupied_boston)
plt.show()


