# import module
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read dataset
boston_dfs = [
    pd.read_csv("./data/" + "boston" + "/ACSDT1Y" + str(year) + ".B25002_data_with_overlays_2021-10-18T223715.csv") for
    year in range(2010, 2020)]
seattle_dfs = [
    pd.read_csv("./data/" + "seattle" + "/ACSDT1Y" + str(year) + ".B25002_data_with_overlays_2021-11-07T181045.csv") for
    year in range(2010, 2020)]
sf_dfs = [pd.read_csv("./data/" + "sf" + "/ACSDT1Y" + str(year) + ".B25002_data_with_overlays_2021-11-07T203134.csv")
          for year in range(2010, 2020)]
philadelphia_dfs = [pd.read_csv(
    "./data/" + "philadelphia" + "/ACSDT1Y" + str(year) + ".B25002_data_with_overlays_2021-11-07T204343.csv") for year
                    in range(2010, 2020)]
portland_dfs = [
    pd.read_csv("./data/" + "portland" + "/ACSDT1Y" + str(year) + ".B25002_data_with_overlays_2021-11-07T205237.csv")
    for year in range(2010, 2020)]

occupied_seattle = []
vacant_seattle = []
occupied_boston = []
vacant_boston = []
occupied_sf = []
vacant_sf = []
occupied_philadelphia = []
vacant_philadelphia = []
occupied_portland = []
vacant_portland = []

for df in seattle_dfs:
    occupied_seattle.append(int(df['B25002_002E'][1]))
    vacant_seattle.append(int(df['B25002_003E'][1]))
for df in boston_dfs:
    occupied_boston.append(int(df['B25002_002E'][2]))
    vacant_boston.append(int(df['B25002_003E'][2]))
for df in sf_dfs:
    occupied_sf.append(int(df['B25002_002E'][1]))
    vacant_sf.append(int(df['B25002_003E'][1]))
for df in philadelphia_dfs:
    occupied_philadelphia.append(int(df['B25002_002E'][1]))
    vacant_philadelphia.append(int(df['B25002_003E'][1]))
for df in portland_dfs:
    occupied_portland.append(int(df['B25002_002E'][1]))
    vacant_portland.append(int(df['B25002_003E'][1]))

# compute the rate of change over the years
roc_vacant_seattle = np.diff(vacant_seattle) / vacant_seattle[:-1]
roc_occupied_seattle = np.diff(occupied_seattle) / occupied_seattle[:-1]
roc_vacant_boston = np.diff(vacant_boston) / vacant_boston[:-1]
roc_occupied_boston = np.diff(occupied_boston) / occupied_boston[:-1]
roc_vacant_sf = np.diff(vacant_sf) / vacant_sf[:-1]
roc_occupied_sf = np.diff(occupied_sf) / occupied_sf[:-1]
roc_vacant_philadelphia = np.diff(vacant_philadelphia) / vacant_philadelphia[:-1]
roc_occupied_philadelphia = np.diff(occupied_philadelphia) / occupied_philadelphia[:-1]
roc_vacant_portland = np.diff(vacant_portland) / vacant_portland[:-1]
roc_occupied_portland = np.diff(occupied_portland) / occupied_portland[:-1]

data = [vacant_portland, occupied_portland]

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
plt.title('Vacant/Occupied in Seattle')

plt.show()

########################################################################################################################

plt.plot([str(year) + "-" + str(year + 1) for year in range(2010, 2019)], roc_vacant_boston, label="Boston")
plt.plot([str(year) + "-" + str(year + 1) for year in range(2010, 2019)], roc_vacant_seattle, label="Seattle")
plt.plot([str(year) + "-" + str(year + 1) for year in range(2010, 2019)], roc_vacant_sf, label="San Francisco")
plt.plot([str(year) + "-" + str(year + 1) for year in range(2010, 2019)], roc_vacant_philadelphia, label="Philadelphia")
plt.plot([str(year) + "-" + str(year + 1) for year in range(2010, 2019)], roc_vacant_portland, label="Portland")

# plt.plot([str(year) + "-" + str(year+1) for year in range(2010, 2019)], roc_occupied_boston, label="Boston")
# plt.plot([str(year) + "-" + str(year+1) for year in range(2010, 2019)], roc_occupied_seattle, label="Seattle")
# plt.plot([str(year) + "-" + str(year+1) for year in range(2010, 2019)], roc_occupied_sf, label="San Francisco")
# plt.plot([str(year) + "-" + str(year+1) for year in range(2010, 2019)], roc_occupied_philadelphia, label="Philadelphia")
# plt.plot([str(year) + "-" + str(year+1) for year in range(2010, 2019)], roc_occupied_portland, label="Portland")
plt.subplots_adjust(left=0.2, bottom=0.2)
plt.xticks([str(year) + "-" + str(year + 1) for year in range(2010, 2019)])
plt.title('rate of change of the number of vacant houses')
plt.legend()
plt.show()

########################################################################################################################

plt.plot(range(2010, 2020), occupied_boston, label="Boston")
plt.plot(range(2010, 2020), occupied_seattle, label="Seattle")
plt.plot(range(2010, 2020), occupied_sf, label="San Francisco")
plt.plot(range(2010, 2020), occupied_philadelphia, label="Philadelphia")
plt.plot(range(2010, 2020), occupied_portland, label="Portland")

# plt.plot(range(2010, 2020), vacant_boston, label="Boston")
# plt.plot(range(2010, 2020), vacant_seattle, label="Seattle")
# plt.plot(range(2010, 2020), vacant_sf, label="San Francisco")
# plt.plot(range(2010, 2020), vacant_philadelphia, label="Philadelphia")
# plt.plot(range(2010, 2020), vacant_portland, label="Portland")

plt.subplots_adjust(left=0.2, bottom=0.2)
plt.xticks(range(2010, 2020))
plt.title('the number of occupied houses')
plt.legend()
plt.show()
