import os
import argparse
import PyPDF2
import textract

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class PdfToWords(object):
    def __init__(self):
        self.currPath = os.getcwd()+"/"
        self.punctuations = ['(',')',';',':','[',']',',']
        self.stop_words = stopwords.words('english')

    def readpdf(self, filename):
        pdfObj = open(filename, "rb")
        pdfReader = PyPDF2.PdfFileReader(pdfObj)
        if pdfReader.isEncrypted:
            try:
                pdfReader.decrypt("")
                print("File Decrypted (PyPDF2)")
            except NotImplementedError:
                command = "cp "+filename+" temp.pdf; qpdf --password='' --decrypt temp.pdf "+filename
                os.system(command)
                print("File Decrypted (qpdf)")
                pdfObj = open(filename, "rb")
                pdfReader = PyPDF2.PdfFileReader(pdfObj)
        else:
            print("File Not Encrypted")
        
        text = ""
        num_pages = pdfReader.numPages
        for den in range(num_pages):
            pageObj = pdfReader.getPage(den)
            text += pageObj.extractText()
        
        if text == "":
            text = textract.process(
                self.currPath+filename, 
                method='tesseract', 
                language='eng')
        
        return text

    def converter(self, filename):
        text = self.readpdf(filename)
        tokens = word_tokenize(text)
        keywords = [word for word in tokens if not word in self.stop_words and not \
            word in self.punctuations]

        return  keywords

if __name__ == "__main__":
    pw = PdfToWords()

    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="choose a file")
    parser.add_argument("-o", "--output", help="insert output filename")
    args = parser.parse_args()

    if args.file:
        keywords = pw.converter(args.file)
        print(keywords)

    if args.output:
        keyfile = open(args.output, "w")
        for word in keywords:
            keyfile.write(word+"\n")