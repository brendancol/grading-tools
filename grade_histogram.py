import os
import pandas

def create_histogram(csv, histoField, outputPath, title, binCount=30):
	df = pandas.read_csv(csv)
	histo = df[histoField].hist(bins=binCount)
	histo.set_title(title)
	histo.set_xlim([20,100])
	histo.set_xlabel('grade')
	histo.set_ylabel('count')

	fig = histo.get_figure()
	fig.savefig(outputPath)
	return outputPath
