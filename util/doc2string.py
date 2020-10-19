import docx

class Document():

  document = None
  string = None

  def __init__(self, path):
    self.document = docx.Document(path)
    self.string = self.build_string()

  def raw_full_text(self):
    raw_full_text = []
    for paragraph in self.document.paragraphs:
        raw_full_text.append(paragraph.text)
    return raw_full_text
  
  def fix_void_paragraph(self, raw_text):
    trimmed_text = []

    for paragraph in raw_text:
      if paragraph != '':
          trimmed_text.append(paragraph)

    return trimmed_text

  def separate_dots(self, string):

    spaces_added = string.replace('.', '. ')
    double_spaces_fixed = spaces_added.replace('  ', ' ')
    return double_spaces_fixed

  
  def merge_string(self, raw_text):
    return ''.join(raw_text)

  def build_string(self):
    return self.separate_dots(
      self.merge_string(
        self.fix_void_paragraph(
          self.raw_full_text()
        )
      )
    )

  

