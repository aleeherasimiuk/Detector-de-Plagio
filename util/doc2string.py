import docx
from util.file_manager import file_extension
from util.other_docs import OtherDoc


class Document():

  type_manager = None
  document = None
  string = None

  def __init__(self, path):
    self.document = self.__get_document(path)
    self.string = self.document.string

  def __get_document(self, path):
    if file_extension(path) == '.doc':
      return Doc(path)
    return Docx(path)


class Docx():

  string = None
  document = None

  def __init__(self, path):
    self.document = self.read_document(path)
    self.string = self.build_string()

  def read_document(self, path):
    return docx.Document(path)

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


class Doc(OtherDoc):

  def __init__(self, path):
    try:
      super().__init__(path, '.doc')
    except:
      super().__init__(path, '.rtf')


