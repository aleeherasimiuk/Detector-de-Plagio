import pandas as pd
import util.file_manager as fm
from document import Document

def save_dataframe(dataframe, path):
  dataframe.to_csv(path)

def get_dataframe(path):
  return pd.read_csv(path)

def get_data(path):
  dataframe = get_dataframe(path)
  dictionary = {}

  for i in range(len(dataframe)):

    serie = dataframe.loc[i]
    document_name = serie.title

    dictionary[document_name] = {}

    document = dictionary[document_name]

    for column in dataframe:
      document[column] = serie[column]

  return dictionary


def delete_dataframe(path):
  fm.delete_file(path)

    
def get_documents(path):
  documents_dictionary = get_data(path)
  return [Document(dictionary = documents_dictionary[d]) for d in documents_dictionary]
