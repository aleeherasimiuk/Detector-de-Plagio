import module_fix
import unittest
import pandas as pd
import numpy as np
from repository.csv_tools import *

class TestCSV(unittest.TestCase):

  array1 = np.zeros(10)
  array2 = np.ones(10)

  dataframe = pd.DataFrame({'array1': array1, 'array2': array2})
  
  def test_save_dataframe_into_csv(self):
    save_dataframe(self.dataframe, 'test.csv')
    self.assertTrue(fm.exists('test.csv'))

    loaded_dataframe = get_dataframe('test.csv')
    self.assertEqual(loaded_dataframe.loc[0]['array1'], self.array1.all())
    self.assertEqual(loaded_dataframe.loc[0]['array2'], self.array2.all())

    delete_dataframe('test.csv')
    self.assertFalse(fm.exists('test.csv'))


if __name__ == '__main__':
    unittest.main()