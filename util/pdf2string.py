from util.generic_document import GenericDocument

class PDF(GenericDocument):

  def __init__(self, path):
    super().__init__(path, '.pdf')
  


