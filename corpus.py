import os
import nltk
import util.file_manager as fm
import re
from util.doc2string import Document
from nltk import word_tokenize

class Corpus():

  string = None 
  tokens = None 
  words  = None 
  types  = None 
  token_ratio = None

  def __init__(self, path):
    self.string = self.get_string(path)
    self.tokens = self.build_tokens()
    self.words  = self.remove_punctuation()
    self.types  = self.remove_duplicated()
    self.token_ratio = self.get_token_ratio()

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
    return self.token_count() / self.type_count()

  def get_string(self, path):
    if not fm.exists(path):
      raise ValueError("Path do not exist: {}".format(path))

    if fm.is_word(path):
      return Document(path).string

