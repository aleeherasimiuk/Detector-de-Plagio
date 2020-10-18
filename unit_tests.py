import unittest
import util.file_manager as fm
from util.doc2string import Document
from corpus import Corpus


class TestFileManager(unittest.TestCase):

  path = 'unit_testing_documents/lorem_ipsum.docx'

  def test_exist(self):
    self.assertTrue(fm.exists(self.path))

  def test_exension(self):
    self.assertEqual(fm.file_extension(self.path), '.docx')

  def test_is_word(self):
    self.assertTrue(fm.is_word(self.path))



class TestDocx(unittest.TestCase):

  corpus = Corpus('unit_testing_documents/lorem_ipsum.docx')

  def test_tokens_are_10978(self):
    self.assertEqual(self.corpus.token_count(), 11206)

  def test_words_are_10000(self):
    self.assertEqual(self.corpus.word_count(), 10000)

  def test_types_are_116(self):
    self.assertEqual(self.corpus.type_count(), 117)

  def test_if_not_exist(self):
    fake_path = 'unit_testing_documents/idontexist.docx'
    self.assertRaises(ValueError, self.corpus.get_string, fake_path)

if __name__ == '__main__':
    unittest.main()