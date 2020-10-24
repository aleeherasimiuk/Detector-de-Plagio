import unittest
import util.file_manager as fm
from util.doc2string import WordDocument
from util.ppt2string import Presentation
from document import Document
import util.log as log
from util.data_cleaning import delete_symbols, remove_multiple_whitespaces, separate_glued_words, merge_string

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

  document = Document('unit_testing_documents/lorem_ipsum.doc')

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

  document = Document('unit_testing_documents/lorem_ipsum.docx')

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

  document = Document('unit_testing_documents/lorem_ipsum.rtf')

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

  document = Document('unit_testing_documents/lorem_ipsum.pptx')
  
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

  document = Document('unit_testing_documents/lorem_ipsum.pdf')

  def test_tokens_are_12176(self):
    self.assertEqual(self.document.token_count(), 12176)

  def test_words_are_10000(self):
    self.assertEqual(self.document.word_count(), 10000)

  def test_types_are_187(self):
    self.assertEqual(self.document.type_count(), 187)

  def test_if_not_exist(self):
    fake_path = 'unit_testing_documents/idontexist.pdf'
    self.assertRaises(ValueError, self.document.get_string, fake_path)


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

if __name__ == '__main__':
    unittest.main()