#!/usr/bin/env python3

import matplotlib.pyplot as plt
import csv

# plt.boxplot

years = ["2017-2018","2018-2019", "2019-2020"]

allData = list()

for year in years:
	risc = list()
	tis = list()
	simd = list()
	total = list()
	with open("{}.csv".format(year), 'r') as f:
		reader = csv.reader(f)
		next(reader)
		for row in reader:
			print(row)
			row = list(map(float, row))
			risc.append(row[0])
			tis.append(row[1])
			simd.append(row[2])
			total.append(row[3])

	yearlyData = [risc, tis, simd, total]
	allData.append(yearlyData)


colors = ["paleturquoise", "lightcoral", "lemonchiffon"]
for i, data in enumerate(allData):
	plt.boxplot(data, patch_artist=True, boxprops=dict(facecolor=colors[i]), medianprops=dict(color="black"), positions=[i+1+y*(len(allData)+1) for y in range(len(data))], showmeans=True, meanline=True)
plt.xticks([2,6,10,14], ['RISC', 'TIS-100', 'SIMD', 'Total'])
plt.figtext(0.35, 0.03, '2017-18', backgroundcolor=colors[0], color='black', size='small')
plt.figtext(0.48, 0.03, '2018-19', backgroundcolor=colors[1], color='black', size='small')
plt.figtext(0.61, 0.03, '2019-20', backgroundcolor=colors[2], color='black', size='small')
plt.title("Évaluation des devoirs de ELECH473")
plt.show()