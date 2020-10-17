import unittest
from doc2string import Document

class TestDocx(unittest.TestCase):

  my_doc = Document('unit_testing_documents/lorem_ipsum.docx')

  def test_tokens_are_10978(self):
    self.assertEqual(self.my_doc.token_count(), 11206)

  def test_words_are_10000(self):
    self.assertEqual(self.my_doc.word_count(), 10000)

    def test_types_are_116(self):
      self.assertEqual(self.my_doc.type_count(), 117)

if __name__ == '__main__':
    unittest.main()