from sklearn.feature_extraction.text import CountVectorizer
from util.data_cleaning import stem_string, lemmatize_word, is_word

class MyCountVectorizer(CountVectorizer):

  lemmatizer = None
  stemmer = None

  def __init__(self, lemmatize = True, stem = False, stop_words = 'spanish'):
    super().__init__(min_df=1, stop_words=stop_words)
    self.lemmatizer = lemmatize_word if lemmatize else self.nothing
    self.stemmer = stem_string if stem else self.nothing

  def build_analyzer(self):
    analyzer = super(MyCountVectorizer, self).build_analyzer()
    return lambda doc: (self.stemmer(self.lemmatizer(w)) for w in analyzer(doc))

  def analyze(self, text):
    analyzer = self.build_analyzer()
    generator = analyzer(text)
    return [word for word in generator]

  def nothing(self, text):
    return text