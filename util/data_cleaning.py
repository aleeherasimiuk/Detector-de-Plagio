import re
from nltk.stem import WordNetLemmatizer, SnowballStemmer

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
      if not re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', token):
          tokens[i] = tokens[i].replace('.', '. ')
  return ' '.join(tokens)
  

def merge_string(splitted_string):
  return ''.join(splitted_string)


stemmer = SnowballStemmer('spanish')

def stem_string(string):
  return stemmer.stem(string)


def lemmatize_string(text):
  return WordNetLemmatizer().lemmatize(text, pos='n')