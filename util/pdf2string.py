from pdfminer.high_level import extract_text

class PDF():

  string = None

  def __init__(self, path):
    self.string = extract_text(path)
