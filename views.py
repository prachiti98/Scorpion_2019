import PyPDF2

cpi = []

pdfobj = open('resume.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfobj)

pageobj = pdfReader.getPage(0)
print(pageobj.extractText())

