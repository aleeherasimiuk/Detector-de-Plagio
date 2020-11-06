import pandas as pd

def get_dataframe(path):
  return pd.read_csv(path)

def get_data(path):
  dataframe = get_dataframe(path)
  dictionary = {}

  for i in range(len(dataframe)):

    serie = dataframe.loc[i]
    document_name = serie.document_title

    dictionary[document_name] = {}

    document = dictionary[document_name]

    for column in dataframe:
      document[column] = serie[column]

  return dictionary

    
