import docx
from util.file_manager import file_extension
from util.file_manager import get_filename
from util.generic_document import GenericDocument
from util.data_cleaning import separate_glued_words
from util.data_cleaning import merge_string
import util.log as log
import re

class WordDocument():

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

    log.debug('Trying to read: {}'.format(get_filename(path)))
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
    return [paragraph for paragraph in raw_text if paragraph != '']
  
  def build_string(self):
    raw_full_text = self.raw_full_text()
    fixed_void_paragraph = self.fix_void_paragraph(raw_full_text)
    merged_string = merge_string(fixed_void_paragraph)
    separated_glued_words = separate_glued_words(merged_string)

    return separated_glued_words



class Doc(GenericDocument):
  def __init__(self, path):
    log.debug('Trying to read: {}'.format(get_filename(path)))
    super().__init__(path, '.doc')


class Rtf(GenericDocument):
  def __init__(self, path):
    log.debug('Trying to read: {}'.format(get_filename(path)))
    super().__init__(path, '.rtf')



