import unittest
from repository.firebase_admin import *

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