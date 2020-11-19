import re
import nltk
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.corpus import stopwords
from es_lemmatizer import lemmatize as __lemmatize
import es_core_news_sm
import util.log as log

nlp = es_core_news_sm.load()
nlp.add_pipe(__lemmatize, after="tagger")
stemmer = SnowballStemmer('spanish')
__stop_words = stopwords.words('spanish')
__stop_words.extend(['mejor', 'primer', 'igual', 'principal', 'total', 'segun', 'según', 'iguales', 'describa', 'hernan', 'borre', 'profesor', 'alumno', 'universidad', 'facultad','regional', 'buenos', 'aires', 'utn', 'www'])


def delete_symbols(string):
  symbols = ['\t', '\n', 'l[pic]', '[pic]', '|', '•', '●', '', '\x0c', '\u200b']
  for symbol in symbols:
    string = string.replace(symbol, ' ')

  return string


def remove_multiple_whitespaces(string):
  return re.sub(' +', ' ', string)


def separate_glued_words(string):
  tokens = string.split(' ')
  for i, token in enumerate(tokens):
      if not is_url(token):
          tokens[i] = tokens[i].replace('.', '. ')
  return ' '.join(tokens)
  

def merge_string(splitted_string):
  return ''.join(splitted_string)

def stem_string(string):
  return stemmer.stem(string)

def is_word(doc):
  if type(doc) == str:
    doc = nlp(doc)[0]
  return doc.lemma_ not in stop_words() and match_word(doc.lemma_) and doc.pos_ not in ('PROPN', 'PUNCT')


def is_useful_sentence(sentence):
  tokens = nltk.word_tokenize(sentence)
  return len(tokens) > 3

def is_name(doc):
  return doc.pos_ == 'PROPN'


def match_word(word):
  return re.match('^[a-z]+$', word)

def ner(sent):
  #is_name(doc) and match_word(doc.lemma_) and doc.lemma_ not in stop_words()
  return [ent.text for ent in nlp(sent).ents if ent.label_ == 'PER' and ent.lemma_ not in stop_words()]

def tokenize_lemmatize_and_tag(text):
  return nlp(text)


def lemmatize_word(word):
  return (tokenize_lemmatize_and_tag(word)[0]).lemma_


def pos_word(word):
  return tokenize_lemmatize_and_tag(word)[0].pos_


def stop_words():
 return __stop_words


def is_email(token):
  return re.search('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', token)


def is_url(token):
  return re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', token)


def is_legajo(token):
  return re.search('[0-9]{3}\.\s?[0-9]{3}-[0-9]', token)


def is_date(token):
  return re.search('[0-9]{2}/[0-9]{2}/[0-9]{4}', token)


def is_course(token):
  return re.search('k[0-9]{4}', token)