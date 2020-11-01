import unittest
import util.file_manager as fm
from util.doc2string import WordDocument
from util.ppt2string import Presentation
from document import Document
import util.log as log
from util.data_cleaning import *
from util.count_vectorizer import MyCountVectorizer
from repository.firebase_admin import *

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

  document = Document('unit_testing_documents/lorem_ipsum.doc', preprocess=False)

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

  document = Document('unit_testing_documents/lorem_ipsum.docx', preprocess=False)

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

  document = Document('unit_testing_documents/lorem_ipsum.rtf', preprocess=False)

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

  document = Document('unit_testing_documents/lorem_ipsum.pptx', preprocess=False)
  
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

  document = Document('unit_testing_documents/lorem_ipsum.pdf', preprocess=False)

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


class TestFirebase(unittest.TestCase):

  fb = Firebase(collection='testing')

  def test_add_document(self):
    self.fb.add_document('TestDocument1', {'Field1': 'Field1Value', 'Field2': 'Field2Value'})
    self.assertTrue(self.fb.document_exists('TestDocument1'))
    result = self.fb.get_document_dict('TestDocument1')
    self.assertEqual([result['Field1'], result['Field2']], ['Field1Value', 'Field2Value'])
    self.fb.delete_document('TestDocument1')
    self.assertFalse(self.fb.document_exists('TestDocument1'))

  def test_add_multiple_documents(self):
    self.fb.add_documents({'TestDocument1': {'Field1': 'Field1Value', 'Field2': 'Field2Value'}, 'TestDocument2': {'Field3': 'Field3Value', 'Field4': 'Field4Value'}})
    self.assertTrue(self.fb.document_exists('TestDocument1'))
    self.assertTrue(self.fb.document_exists('TestDocument2'))
    result1 = self.fb.get_document_dict('TestDocument1')
    result2 = self.fb.get_document_dict('TestDocument2')
    self.assertEqual([result1['Field1'], result1['Field2']], ['Field1Value', 'Field2Value'])
    self.assertEqual([result2['Field3'], result2['Field4']], ['Field3Value', 'Field4Value'])
    self.fb.delete_document('TestDocument1')
    self.fb.delete_document('TestDocument2')
    self.assertFalse(self.fb.document_exists('TestDocument1'))
    self.assertFalse(self.fb.document_exists('TestDocument2'))

if __name__ == '__main__':
    unittest.main()