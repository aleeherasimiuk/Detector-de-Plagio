import re
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.corpus import stopwords
from es_lemmatizer import lemmatize as __lemmatize
import es_core_news_sm
import util.log as log

nlp = es_core_news_sm.load()
nlp.add_pipe(__lemmatize, after="tagger")
stemmer = SnowballStemmer('spanish')
__stop_words = stopwords.words('spanish')
__stop_words.extend(['mejor', 'primer', 'igual', 'principal', 'total', 'segun', 'según', 'iguales', 'describa', 'hernan', 'borre', 'profesor', 'alumno', 'universidad', 'facultad','regional', 'buenos', 'aires', 'utn'])
  


def delete_symbols(string):
  symbols = ['\t', '\n', 'l[pic]', '[pic]', '|', '•', '●', '', '\x0c']
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


def preprocess(text):
  return [word.lemma_ for word in tokenize_lemmatize_and_tag(text.lower()) if is_word(word)]


def is_word(doc):
  #return word not in stop_words() and re.match('\w', word) and len(word) > 3 and not is_url(word) and not is_email(word) and not is_legajo(word) and not is_course(word) and not is_date(word)
  return doc.lemma_ not in stop_words() and re.match('^[a-z]+$', doc.lemma_) and doc.pos_ not in ('PROPN', 'PUNCT')

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