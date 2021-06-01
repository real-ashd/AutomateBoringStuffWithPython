#Reading And Editing PDFs
#PDF is a binary file so it can't be read in simple text format
#It can't open all the pdfs
#We use module PyPDF2
#Install it using 'pip install PyPDF2'

import PyPDF2
#It can extract text from pdf
pdfFile = open('meetingminutes.pdf','rb')
reader = PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages)
page = reader.getPage(0)
print(page.extractText())

#Extracting all pages in text format using for loop
for pageNum in range(reader.numPages):
	print(reader.getPage(pageNum).extractText())
pdfFile.close()
print("-----------------------------------------------")

#Combining two pdfs at page Level
pdfFile1 = open('meetingminutes1.pdf','rb')
pdfFile2 = open('meetingminutes2.pdf','rb')
reader1 = PyPDF2.PdfFileReader(pdfFile1)
reader2 = PyPDF2.PdfFileReader(pdfFile2)
writer = PyPDF2.PdfFileWriter()
#Now this is a blank page pdf

for pageNum in range(reader1.numPages):
	page = reader1.getPage(pageNum)
	writer.addPage(page)

for pageNum in range(reader2.numPages):
	page = reader2.getPage(pageNum)
	writer.addPage(page)

print("writer object has the new pdf contents.\nNow we save it to a file combineminutes.pdf")

outputFile = open('combineminutes.pdf','wb')
writer.write(outputFile)
outputFile.close()
pdfFile1.close()
pdfFile2.close()
print("Done!")