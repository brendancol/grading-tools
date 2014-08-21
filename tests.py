import os
import sys
import unittest
import grade_histogram

class GradingToolTests(unittest.TestCase):

	def setUp(self):
		self.data_directory = os.path.join(sys.path[0], 'test_data')
		self.output_directory = os.path.join(sys.path[0], 'test_output')

	def tearDown(self):
		pass

	def test_create_histogram_csv(self):
		grades_csv = os.path.join(self.data_directory,'grades.csv')
		grade_field = 'grades'
		output = os.path.join(self.output_directory, 'test_histogram.png')
		
		success = grade_histogram.create_histogram(grades_csv, grade_field, output, 'Grades PNG')
		self.assertTrue(success)

		output = os.path.join(self.output_directory, 'test_histogram.pdf')
		success = grade_histogram.create_histogram(grades_csv, grade_field, output, 'Grades PDF')
		self.assertTrue(success)

		output = os.path.join(self.output_directory, 'test_histogram.jpg')
		success = grade_histogram.create_histogram(grades_csv, grade_field, output, 'Grades JPG')
		self.assertTrue(success)

	def test_create_histogram_xls(self):
		grades_csv = os.path.join(self.data_directory,'grades.xls')
		grade_field = 'grades'
		output = os.path.join(self.output_directory, 'test_histogram.png')
		
		success = grade_histogram.create_histogram(grades_csv, grade_field, output, 'Grades PNG')
		self.assertTrue(success)

		output = os.path.join(self.output_directory, 'test_histogram.pdf')
		success = grade_histogram.create_histogram(grades_csv, grade_field, output, 'Grades PDF')
		self.assertTrue(success)

		output = os.path.join(self.output_directory, 'test_histogram.jpg')
		success = grade_histogram.create_histogram(grades_csv, grade_field, output, 'Grades JPG')
		self.assertTrue(success)

	def test_create_histogram_xlsx(self):
		grades_csv = os.path.join(self.data_directory,'grades.xlsx')
		grade_field = 'grades'
		output = os.path.join(self.output_directory, 'test_histogram.png')
		
		success = grade_histogram.create_histogram(grades_csv, grade_field, output, 'Grades PNG')
		self.assertTrue(success)

		output = os.path.join(self.output_directory, 'test_histogram.pdf')
		success = grade_histogram.create_histogram(grades_csv, grade_field, output, 'Grades PDF')
		self.assertTrue(success)

		output = os.path.join(self.output_directory, 'test_histogram.jpg')
		success = grade_histogram.create_histogram(grades_csv, grade_field, output, 'Grades JPG')
		self.assertTrue(success)

if __name__ == '__main__':
	unittest.main()
