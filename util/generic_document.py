import textract
import util.log as log
from util.file_manager import get_filename
from textract.exceptions import ShellError
from util.exceptions import InvalidDocument

class GenericDocument():

  string = None

  def __init__(self, path, extension):
    try:
      self.string = self.read_document(path, extension)
    except:
      log.error('There was an error reading: {}, document will be ignored and an exception was thrown. Catch it!'.format(get_filename(path)))
      raise InvalidDocument()    

  def read_document(self, path, extension):
    return self.decode_text(self.extract_text(path, extension))

  def decode_text(self, encoded_document):
    return encoded_document.decode('UTF-8')

  def extract_text(self, path, extension):
    return textract.process(path, extension = extension)


