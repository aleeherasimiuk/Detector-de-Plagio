from util.generic_document import GenericDocument
import textract
import re

class PDF(GenericDocument):

  def __init__(self, path):
    super().__init__(path, '.pdf')
  
  def extract_text(self, path, extension):
    return textract.process(path, extension = extension, method='pdftotext')

  def get_paragraphs(self):
    return re.split('\.\n', self.string)


