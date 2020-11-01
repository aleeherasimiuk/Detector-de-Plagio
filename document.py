import os
import nltk
import util.file_manager as fm
import re
from util.doc2string import WordDocument
from util.ppt2string import Presentation
from util.pdf2string import PDF
from util.doc2string import Rtf
from util.generic_document import GenericDocument
from nltk import word_tokenize, sent_tokenize
import util.log as log
from util.exceptions import InvalidDocument
from util.data_cleaning import delete_symbols, remove_multiple_whitespaces, tokenize_lemmatize_and_tag, is_word, tag_words, ner
from util.count_vectorizer import MyCountVectorizer

class Document():

  string = None 
  tokens = None 
  words  = None 
  types  = None
  tagged = [] 
  token_ratio                = None
  lemmatized_string          = None
  stemmed_string             = None
  simple_preprocessed_string = None

  sentences = [] 
  named_entities = []

  def __init__(self, path, preprocess = True):
    self.string = self.get_string(path)
    self.clean_dataset()
    self.tokens = self.build_tokens()
    self.words  = self.remove_punctuation()
    self.types  = self.remove_duplicated()
    self.token_ratio = self.get_token_ratio()
    self.sentences = self.build_sentences()
    
    if preprocess:
      self.preprocess()

    self.log_results(path)

  def clean_dataset(self):
    self.string = delete_symbols(self.string)
    self.string = remove_multiple_whitespaces(self.string)

  def build_tokens(self):
    return word_tokenize(self.string)

  def build_sentences(self):
    return sent_tokenize(self.string)

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

  def preprocess(self):
    self.lemmatized_string = self.lemmatized_preprocessing()
    self.stemmed_string = self.stemmed_preprocessing()
    self.simple_preprocessed_string = self.simple_preprocessing()
    self.tagged = tag_words(self.string.lower())
    self.named_entities = self.name_entity_recognition()


#  def preprocess(self):
#    return [self.process_word(word) for word in tokenize_lemmatize_and_tag(self.string.lower()) if is_word(word)]

#def process_word(self, word):
#   return word.lemma_


  def lemmatized_preprocessing(self):
    vectorizer = MyCountVectorizer(lemmatize=True, stem=False)
    return vectorizer.analyze(self.string)

  def stemmed_preprocessing(self):
    vectorizer = MyCountVectorizer(lemmatize=True, stem=True)
    return vectorizer.analyze(self.string)

  def simple_preprocessing(self):
    vectorizer = MyCountVectorizer(lemmatize=False, stem=False)
    return vectorizer.analyze(self.string)

  def name_entity_recognition(self):
    entities = []
    for sentence in self.sentences:
      entities.extend(ner(sentence))

    return entities

  def get_string(self, path):
    if not fm.exists(path):
      log.error('There was an error reading: {}, path do not exist. An exception was thrown. Catch it!'.format(fm.get_filename(path)))
      raise ValueError("Path do not exist: {}".format(path))

    if fm.is_rtf(path):
      return Rtf(path).string

    if fm.is_word(path):
      return WordDocument(path).string

    if fm.is_presentation(path):
      return Presentation(path).string

    if fm.is_pdf(path):
      return PDF(path).string

    raise InvalidDocument()

  def log_results(self, path):
    log.info('Document has been read succesfully -> {}\n\tWords: {}\n\tTokens: {}\n\tTypes: {}\n\tToken Ratio: {}'.format(fm.get_filename(path), len(self.words), len(self.tokens), len(self.types), self.token_ratio))

