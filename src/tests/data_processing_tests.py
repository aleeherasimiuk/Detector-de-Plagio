import module_fix
import unittest
from util.data_cleaning import *
from util.count_vectorizer import MyCountVectorizer

class DataCleaning(unittest.TestCase):

  string_with_symbols = 'Lorem\t ipsum dolor sit \n amet, Lorem l[pic] ipsum [pic] | dolor sit amet • ●  \x0c'
  string_without_symbols = 'Lorem ipsum dolor sit amet, Lorem ipsum dolor sit amet '

  def test_remove_symbols_and_multiple_whitespaces(self):
    test_string_without_symbols = delete_symbols(self.string_with_symbols)
    test_string_without_spaces = remove_multiple_whitespaces(test_string_without_symbols)

    self.assertEqual(test_string_without_spaces, self.string_without_symbols)

  string_with_glued_words = 'test.string with glued.words and a very simple URL: https://www.google.com.ar'
  string_without_glued_words = 'test. string with glued words and a very simple URL: https://www.google.com.ar'

  def test_remove_glued_words(self):
    test_string_without_glued_words = separate_glued_words(self.string_with_glued_words)
    self.assertEqual(self.string_without_glued_words, test_string_without_glued_words)

  string_with_glued_words = 'test.string with glued.words and a very simple URL: http://www.google.com.ar/test/testing/do_not_break_url'
  string_without_glued_words = 'test. string with glued. words and a very simple URL: http://www.google.com.ar/test/testing/do_not_break_url'

  def test_do_not_break_urls(self):
    test_string_without_glued_words = separate_glued_words(self.string_with_glued_words)
    self.assertEqual(self.string_without_glued_words, test_string_without_glued_words)

  splitted_string = ['Lorem ipsum dolor sit amet, ', 'Lorem ipsum dolor sit amet']
  merged_string = 'Lorem ipsum dolor sit amet, Lorem ipsum dolor sit amet'

  def test_merge_string(self):
    test_merged_string = merge_string(self.splitted_string)
    self.assertEqual(test_merged_string, self.merged_string)

  def test_lemmatize(self):
    self.assertEqual(lemmatize_word('clientes'), 'cliente')

  def test_is_email(self):
    self.assertTrue(is_email('jhondoe@example.com'))

  def test_is_legajo(self):
    self.assertTrue(is_legajo('146.566-1'))

  def test_is_legajo_typo(self):
    self.assertTrue(is_legajo('167. 251-4'))

  def test_is_url(self):
    self.assertTrue(is_url('https://google.com'))

  def test_is_date(self):
    self.assertTrue(is_date('31/12/2020'))


class TestCountVectorizer(unittest.TestCase):
  string = 'Juan fue a comprar mandarinas y cebollas'

  vectorizer = MyCountVectorizer(lemmatize=True, stem = False, stop_words = stop_words())

  def test_vectorizer(self):
    result = self.vectorizer.analyze(self.string)
    self.assertEqual(result, ['comprar', 'mandarina', 'cebolla'])


if __name__ == '__main__':
    unittest.main()