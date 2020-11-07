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
from util.data_cleaning import delete_symbols, remove_multiple_whitespaces, tokenize_lemmatize_and_tag, is_word, ner
from util.count_vectorizer import MyCountVectorizer
import multiprocessing
from multiprocessing import Process, Value
from util.exceptions import DoubleSource
import ujson

class Document():

  title    = None
  topic    = None
  string   = None 
  tokens   = None 
  words    = None 
  types    = None
  bigrams  = None
  trigrams = None
  initialized         = False
  token_ratio         = None
  lemmatized_string   = None
  lemmatized_bigrams  = None
  lemmatized_trigrams = None
  stemmed_string      = None
  stemmed_bigrams     = None
  stemmed_trigrams    = None
  simple_preprocessed_string   = None
  simple_preprocessed_bigrams  = None
  simple_preprocessed_trigrams = None

  tagged          = [] 
  sentences       = [] 
  named_entities  = []


  def __init__(self, path = None, dictionary = None, preprocess = True):

    if path and dictionary:
      raise DoubleSource()

    if path:
      self.from_file(path, preprocess)
      self.initalized = True 

    if dictionary:
      self.from_dict(dictionary)
      self.initalized = True 

  def from_dict(self, dict):
    self.topic     = self.__value(dict,'topic')
    self.string    = self.__value(dict,'string')
    self.bigrams   = dict['tokens_bigrams']
    self.trigrams  = dict['tokens_trigrams']
    self.sentences = dict['sentences']
    self.title     = self.__value(dict,'document_title')
    self.stemmed_string      = self.__value(dict,'stemmed_text')
    self.named_entities      = dict['named_entities']
    self.lemmatized_string   = self.__value(dict,'lemmatized_text')
    self.stemmed_bigrams     = dict['stemmed_bigrams']
    self.stemmed_trigrams    = dict['stemmed_trigrams']
    self.lemmatized_trigams  = dict['lemmatized_trigrams']
    self.lemmatized_bigrams  = dict['lemmatized_bigrams']
    self.simple_preprocessed_string   = self.__value(dict,'simple_preprocessed')
    self.simple_preprocessed_bigrams  = dict['simple_preprocessed_bigrams']
    self.simple_preprocessed_trigrams = dict['simple_preprocessed_trigrams']

  
  def __value(self, dict, key):
    return ujson.loads(dict[key].replace("'", '"')) if dict[key][0] == '[' else dict[key]
  

  def from_file(self, path, preprocess=True):
    self.string = self.get_string(path)
    self.clean_dataset()
    self.tokens = self.build_tokens()
    self.words  = self.remove_punctuation()
    self.types  = self.remove_duplicated()
    self.token_ratio = self.get_token_ratio()
    self.sentences = self.build_sentences()
    self.title = self.get_title(path)
    
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
    self.lemmatized_string            = self.lemmatized_preprocessing()
    self.stemmed_string               = self.stemmed_preprocessing()
    self.simple_preprocessed_string   = self.simple_preprocessing()
    self.named_entities               = self.name_entity_recognition(include_title=True)

    self.bigrams                      = self.make_bigrams(self.tokens)
    self.lemmatized_bigrams           = self.make_bigrams(self.lemmatized_string)
    self.stemmed_bigrams              = self.make_bigrams(self.stemmed_string)
    self.simple_preprocessed_bigrams  = self.make_bigrams(self.simple_preprocessed_string)
    self.trigrams                     = self.make_trigrams(self.tokens)
    self.lemmatized_trigrams          = self.make_trigrams(self.lemmatized_string)
    self.stemmed_trigrams             = self.make_trigrams(self.stemmed_string)
    self.simple_preprocessed_trigrams = self.make_trigrams(self.simple_preprocessed_string)


  def lemmatized_preprocessing(self):
    vectorizer = MyCountVectorizer(lemmatize=True, stem=False)
    return vectorizer.analyze(self.string)

  def stemmed_preprocessing(self):
    vectorizer = MyCountVectorizer(lemmatize=True, stem=True)
    return vectorizer.analyze(self.string)

  def simple_preprocessing(self):
    vectorizer = MyCountVectorizer(lemmatize=False, stem=False)
    return vectorizer.analyze(self.string)

  def name_entity_recognition(self, include_title = False):
    entities = []
    for sentence in self.sentences:
      entities.extend(ner(sentence))

    if include_title:
      entities.extend(ner(self.title.replace('_', ' ').replace('-', ' ')))

    return entities

  def make_bigrams(self, tokens):
    return list(nltk.bigrams(tokens))

  def make_trigrams(self, tokens):
    return list(nltk.trigrams(tokens))

  def get_title(self, path):
    return fm.get_filename(path).split('.')[0]

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


  def get_topic(self):
    topic if topic else 'Unknown'

