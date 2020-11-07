import module_fix
import unittest
import util.file_manager as fm

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


if __name__ == '__main__':
    unittest.main()