import os
import pandas

def create_histogram(inputFile, histoField, outputPath, title, binCount=30):
	if '.csv' in inputFile:
		dataframe = pandas.read_csv(inputFile)
	elif '.xls' in inputFile:
		dataframe = pandas.read_excel(inputFile)
		
	data = dataframe[histoField]
	histo = data.hist(bins=binCount)
	histo.set_title(title)
	histo.set_xlim([20,100])
	histo.set_xlabel('grade')
	histo.set_ylabel('count')

	fig = histo.get_figure()
	fig.savefig(outputPath)
	return outputPath
