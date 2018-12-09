# import pandas as pd
# import tabula
# files = "test.pdf"
# # path ="C://vedant//DataScienceProject//StudyMaterial//" + files
# path = files
# df = tabula.read_pdf(path, pages = '2', multiple_tables = True)
# print(df)


#importing all the required modules
import PyPDF2

# creating an object
file = open('test.pdf', 'rb')

# creating a pdf reader object
fileReader = PyPDF2.PdfFileReader(file)

# print the number of pages in pdf file
print(fileReader.pages)