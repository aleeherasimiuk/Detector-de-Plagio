import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import util.log as log

class Firebase():

  collection = None
  cred = None
  db = None

  def __init__(self, collection = 'dataset'):
    self.collection = collection
    try:
      self.cred = credentials.Certificate("service_account_key.json")
      firebase_admin.initialize_app(self.cred)
      self.db = firestore.client()
    except FileNotFoundError:
      log.error('There is no service account key file for Firebase Keys. Please put it in root directory of this project')

  def get_collection(self):
    return self.db.collection(self.collection)

  def __get_document(self, title):
    return self.get_collection().document(title)

  def add_document(self, title, data):
    self.__get_document(title).set(data)

  def add_documents(self, data):
    [self.add_document(key, data[key]) for key in data]

  def get_documents(self):
    return self.get_collection().stream()

  def get_documents_dict(self):
    return [doc.to_dict() for doc in self.get_documents()]

  def get_document(self, title):
    return self.__get_document(title).get()

  def get_document_dict(self, title):
    return self.get_document(title).to_dict()

  def document_exists(self, title):
    return self.get_document(title).exists

  def get_document_field(self, title, field):
    return self.__get_document(title)[field]

  def delete_document(self, title):
    self.__get_document(title).delete()