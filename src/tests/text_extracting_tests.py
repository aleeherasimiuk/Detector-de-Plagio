import module_fix
import unittest
from util.doc2string import WordDocument
from util.ppt2string import Presentation
from document import Document
import util.log as log
log.init_logger()

class TestDoc(unittest.TestCase):

  document = Document(path='unit_testing_documents/lorem_ipsum.doc', preprocess=False)

  def test_tokens_are_12176(self):
    self.assertEqual(self.document.token_count(), 12176)

  def test_words_are_10000(self):
    self.assertEqual(self.document.word_count(), 10000)

  def test_types_are_187(self):
    self.assertEqual(self.document.type_count(), 187)

  def test_if_not_exist(self):
    fake_path = 'unit_testing_documents/idontexist.doc'
    self.assertRaises(ValueError, self.document.get_string, fake_path)

class TestDocx(unittest.TestCase):

  document = Document(path='unit_testing_documents/lorem_ipsum.docx', preprocess=False)

  def test_tokens_are_12176(self):
    self.assertEqual(self.document.token_count(), 12176)

  def test_words_are_10000(self):
    self.assertEqual(self.document.word_count(), 10000)

  def test_types_are_187(self):
    self.assertEqual(self.document.type_count(), 187)

  def test_if_not_exist(self):
    fake_path = 'unit_testing_documents/idontexist.docx'
    self.assertRaises(ValueError, self.document.get_string, fake_path)


class TestRtf(unittest.TestCase):

  document = Document(path='unit_testing_documents/lorem_ipsum.rtf', preprocess=False)

  def test_tokens_are_12176(self):
    self.assertEqual(self.document.token_count(), 12176)

  def test_words_are_10000(self):
    self.assertEqual(self.document.word_count(), 10000)

  def test_types_are_187(self):
    self.assertEqual(self.document.type_count(), 187)

  def test_if_not_exist(self):
    fake_path = 'unit_testing_documents/idontexist.rtf'
    self.assertRaises(ValueError, self.document.get_string, fake_path)


class TestPresentation(unittest.TestCase):

  document = Document(path='unit_testing_documents/lorem_ipsum.pptx', preprocess=False)
  
  def test_tokens_are_12176(self):
    self.assertEqual(self.document.token_count(), 12176)

  def test_words_are_10000(self):
    self.assertEqual(self.document.word_count(), 10000)

  def test_types_are_187(self):
    self.assertEqual(self.document.type_count(), 187)

  def test_if_not_exist(self):
    fake_path = 'unit_testing_documents/idontexist.pptx'
    self.assertRaises(ValueError, self.document.get_string, fake_path)


class TestPdf(unittest.TestCase):

  document = Document(path='unit_testing_documents/lorem_ipsum.pdf', preprocess=False)

  def test_tokens_are_12176(self):
    self.assertEqual(self.document.token_count(), 12176)

  def test_words_are_10000(self):
    self.assertEqual(self.document.word_count(), 10000)

  def test_types_are_187(self):
    self.assertEqual(self.document.type_count(), 187)

  def test_if_not_exist(self):
    fake_path = 'unit_testing_documents/idontexist.pdf'
    self.assertRaises(ValueError, self.document.get_string, fake_path)


if __name__ == '__main__':
    unittest.main()