import module_fix
import unittest
from document import Document 


class TestDictionaryProcessing(unittest.TestCase):

  dictionary = {
    'topic':  'this is a topic',
    'string': 'this is a string',
    'bigrams': "[('word1','word2'), ('word2','word3'), ('word3','word4'), ('word4','word5')]",
    'trigrams': "[('word1','word2', 'word3'), ('word3', 'word4', 'word5'), ('word4', 'word5', 'word6'), ('word6','word7', 'word8')]",
    'sentences': "['this is a sentence', 'this is another sentence']",
    'preprocessed_sentences': "['this is a sentence', 'this is another sentence']",
    'title': 'this is a title',
    'stemmed_string': "['word1', 'word2']",
    'lemmatized_string': "['word1', 'word2']",
    'named_entities': "['word1', 'word2']",
    'lemmatized_bigrams': "[('word1','word2'), ('word2','word3'), ('word3','word4'), ('word4','word5')]",
    'stemmed_bigrams': "[('word1','word2'), ('word2','word3'), ('word3','word4'), ('word4','word5')]",
    'lemmatized_trigrams': "[('word1','word2', 'word3'), ('word3', 'word4', 'word5'), ('word4', 'word5', 'word6'), ('word6','word7', 'word8')]",
    'stemmed_trigrams': "[('word1','word2', 'word3'), ('word3', 'word4', 'word5'), ('word4', 'word5', 'word6'), ('word6','word7', 'word8')]",
    'simple_preprocessed_string': "['word1', 'word2']",
    'simple_preprocessed_bigrams': "[('word1','word2'), ('word2','word3'), ('word3','word4'), ('word4','word5')]",
    'simple_preprocessed_trigrams': "[('word1','word2', 'word3'), ('word3', 'word4', 'word5'), ('word4', 'word5', 'word6'), ('word6','word7', 'word8')]",
    'paragraphs': "['this is a paragraph', 'this is another paragraph']",
    'preprocessed_paragraphs': "['this is a paragraph', 'this is another paragraph']",
  }

  document = Document(dictionary = dictionary, preprocess=False)

  def test_topic(self):
    self.assertEqual(self.document.topic, 'this is a topic')

  def test_string(self):
    self.assertEqual(self.document.string, 'this is a string')

  def test_bigrams(self):
    self.assertEqual(self.document.bigrams, [('word1','word2'), ('word2','word3'), ('word3','word4'), ('word4','word5')])

  def test_trigrams(self):
    self.assertEqual(self.document.trigrams, [('word1','word2', 'word3'), ('word3', 'word4', 'word5'), ('word4', 'word5', 'word6'), ('word6','word7', 'word8')])

  def test_sentences(self):
     self.assertEqual(self.document.sentences, ['this is a sentence', 'this is another sentence'])

  def test_title(self):
    self.assertEqual(self.document.title, 'this is a title')

  def test_stemmed_text(self):
    self.assertEqual(self.document.stemmed_string, ['word1', 'word2'])

  def test_lemmatized_text(self):
    self.assertEqual(self.document.lemmatized_string, ['word1', 'word2'])

  def test_named_entities(self):
    self.assertEqual(self.document.named_entities, ['word1', 'word2'])

  def test_lemmatized_bigrams(self):
    self.assertEqual(self.document.lemmatized_bigrams, [('word1','word2'), ('word2','word3'), ('word3','word4'), ('word4','word5')])

  def test_lemmatized_trigrams(self):
    self.assertEqual(self.document.lemmatized_trigams, [('word1','word2', 'word3'), ('word3', 'word4', 'word5'), ('word4', 'word5', 'word6'), ('word6','word7', 'word8')])

  def test_stemmed_bigrams(self):
    self.assertEqual(self.document.stemmed_bigrams, [('word1','word2'), ('word2','word3'), ('word3','word4'), ('word4','word5')])

  def test_stemmed_trigrams(self):
    self.assertEqual(self.document.stemmed_trigrams, [('word1','word2', 'word3'), ('word3', 'word4', 'word5'), ('word4', 'word5', 'word6'), ('word6','word7', 'word8')])

  def test_simple_preprocessed_text(self):
    self.assertEqual(self.document.simple_preprocessed_string, ['word1', 'word2'])

  def test_simple_preprocessed_bigrams(self):
    self.assertEqual(self.document.simple_preprocessed_bigrams, [('word1','word2'), ('word2','word3'), ('word3','word4'), ('word4','word5')])

  def test_simple_preprocessed_trigrams(self):
    self.assertEqual(self.document.simple_preprocessed_trigrams, [('word1','word2', 'word3'), ('word3', 'word4', 'word5'), ('word4', 'word5', 'word6'), ('word6','word7', 'word8')])

  def test_preprocessed_sentences(self):
    self.assertEqual(self.document.preprocessed_sentences, ['this is a sentence', 'this is another sentence'])

  def test_paragraphs(self):
    self.assertEqual(self.document.paragraphs, ['this is a paragraph', 'this is another paragraph'])
  
  def test_preprocessed_paragraphs(self):
     self.assertEqual(self.document.preprocessed_paragraphs, ['this is a paragraph', 'this is another paragraph'])

if __name__ == '__main__':
    unittest.main()