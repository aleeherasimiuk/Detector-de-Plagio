import os
import nltk
import util.file_manager as fm
import re
from util.doc2string import Document
from util.ppt2string import Presentation
from util.pdf2string import PDF
from util.doc2string import Rtf
from util.other_docs import OtherDoc
from nltk import word_tokenize
import util.log as log
from util.exceptions import InvalidDocument

class Corpus():

  string = None 
  tokens = None 
  words  = None 
  types  = None 
  token_ratio = None

  def __init__(self, path):
    self.string = self.get_string(path)
    self.clean_dataset()
    self.tokens = self.build_tokens()
    self.words  = self.remove_punctuation()
    self.types  = self.remove_duplicated()
    self.token_ratio = self.get_token_ratio()

    self.log_results(path)

  def clean_dataset(self):
    symbols = ['\t', '\n', 'l[pic]', '[pic]', '|', '•', '●', '']
    for symbol in symbols:
      self.string = self.string.replace(symbol, ' ')

    self.remove_multiple_whitespaces()

  def remove_multiple_whitespaces(self):
    self.string = re.sub(' +', ' ', self.string)

  def build_tokens(self):
    return word_tokenize(self.string)

  def remove_punctuation(self):
    return [word.lower() for word in self.tokens if re.search("\w", word)]

  def remove_duplicated(self):
    return set(self.words)

  def token_count(self):
    return len(self.tokens)

  def word_count(self):
    return len(self.words)

  def type_count(self):
    return len(self.types)

  def get_token_ratio(self):
    return self.type_count() / self.token_count()

  def get_string(self, path):
    if not fm.exists(path):
      raise ValueError("Path do not exist: {}".format(path))

    if fm.is_rtf(path):
      return Rtf(path).string

    if fm.is_word(path):
      return Document(path).string

    if fm.is_presentation(path):
      return Presentation(path).string

    if fm.is_pdf(path):
      return PDF(path).string

    raise InvalidDocument()

  def log_results(self, path):
    log.info('Document has been read succesfully -> {}\n\tWords: {}\n\tTokens: {}\n\tTypes: {}\n\tToken Ratio: {}'.format(fm.get_filename(path), len(self.words), len(self.tokens), len(self.types), self.token_ratio))

