import unittest
import util.file_manager as fm
from util.doc2string import Document
from util.ppt2string import Presentation
from corpus import Corpus
import util.log as log

log.init_logger()


class TestFileManager(unittest.TestCase):

  doc_path = 'unit_testing_documents/lorem_ipsum.docx'

  def test_doc_exist(self):
    self.assertTrue(fm.exists(self.doc_path))

  def test_exension_is_docx(self):
    self.assertEqual(fm.file_extension(self.doc_path), '.docx')

  def test_is_word(self):
    self.assertTrue(fm.is_word(self.doc_path))

  ppt_path = 'unit_testing_documents/lorem_ipsum.pptx'

  def test_ppt_exist(self):
    self.assertTrue(fm.exists(self.ppt_path))

  def test_exension_is_pptx(self):
    self.assertEqual(fm.file_extension(self.ppt_path), '.pptx')

  def test_is_pptx(self):
    self.assertTrue(fm.is_presentation(self.ppt_path))

  def test_is_rtf(self):
    self.assertTrue(fm.is_rtf('unit_testing_documents/lorem_ipsum.rtf'))

  def test_is_not_rtf(self):
    self.assertFalse(fm.is_rtf('unit_testing_documents/lorem_ipsum.doc'))


class TestDoc(unittest.TestCase):

  corpus = Corpus('unit_testing_documents/lorem_ipsum.doc')

  def test_tokens_are_12176(self):
    self.assertEqual(self.corpus.token_count(), 12176)

  def test_words_are_10000(self):
    self.assertEqual(self.corpus.word_count(), 10000)

  def test_types_are_187(self):
    self.assertEqual(self.corpus.type_count(), 187)

  def test_if_not_exist(self):
    fake_path = 'unit_testing_documents/idontexist.doc'
    self.assertRaises(ValueError, self.corpus.get_string, fake_path)

class TestDocx(unittest.TestCase):

  corpus = Corpus('unit_testing_documents/lorem_ipsum.docx')

  def test_tokens_are_12176(self):
    self.assertEqual(self.corpus.token_count(), 12176)

  def test_words_are_10000(self):
    self.assertEqual(self.corpus.word_count(), 10000)

  def test_types_are_187(self):
    self.assertEqual(self.corpus.type_count(), 187)

  def test_if_not_exist(self):
    fake_path = 'unit_testing_documents/idontexist.docx'
    self.assertRaises(ValueError, self.corpus.get_string, fake_path)


class TestRtf(unittest.TestCase):

  corpus = Corpus('unit_testing_documents/lorem_ipsum.rtf')

  def test_tokens_are_12176(self):
    self.assertEqual(self.corpus.token_count(), 12176)

  def test_words_are_10000(self):
    self.assertEqual(self.corpus.word_count(), 10000)

  def test_types_are_187(self):
    self.assertEqual(self.corpus.type_count(), 187)

  def test_if_not_exist(self):
    fake_path = 'unit_testing_documents/idontexist.rtf'
    self.assertRaises(ValueError, self.corpus.get_string, fake_path)


class TestPresentation(unittest.TestCase):

  corpus = Corpus('unit_testing_documents/lorem_ipsum.pptx')
  
  def test_tokens_are_12176(self):
    self.assertEqual(self.corpus.token_count(), 12176)

  def test_words_are_10000(self):
    self.assertEqual(self.corpus.word_count(), 10000)

  def test_types_are_187(self):
    self.assertEqual(self.corpus.type_count(), 187)

  def test_if_not_exist(self):
    fake_path = 'unit_testing_documents/idontexist.pptx'
    self.assertRaises(ValueError, self.corpus.get_string, fake_path)


class TestPdf(unittest.TestCase):

  corpus = Corpus('unit_testing_documents/lorem_ipsum.pdf')

  def test_tokens_are_12176(self):
    self.assertEqual(self.corpus.token_count(), 12176)

  def test_words_are_10000(self):
    self.assertEqual(self.corpus.word_count(), 10000)

  def test_types_are_187(self):
    self.assertEqual(self.corpus.type_count(), 187)

  def test_if_not_exist(self):
    fake_path = 'unit_testing_documents/idontexist.pdf'
    self.assertRaises(ValueError, self.corpus.get_string, fake_path)

if __name__ == '__main__':
    unittest.main()