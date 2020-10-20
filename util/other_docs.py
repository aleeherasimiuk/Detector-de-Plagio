import textract

class OtherDoc():

  string = None

  def __init__(self, path, extension):
    self.string = self.read_document(path, extension)

  def read_document(self, path, extension):
    return self.decode_text(self.extract_text(path, extension))

  def decode_text(self, encoded_document):
    return encoded_document.decode('UTF-8')

  def extract_text(self, path, extension):
    return textract.process(path, extension = extension)