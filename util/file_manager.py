import os

def exists(path):
  return os.path.exists(path)

def file_extension(path):
  _, ext = os.path.splitext(path)
  return ext

def is_word(path):
  return file_extension(path) in ('.doc', '.docx', '.odt')

def is_presentation(path):
  return file_extension(path) in ('.ppt', '.pptx', '.odf')

def is_pdf(path):
  return file_extension(path) == '.pdf'

def get_filename(path):
  filename = os.path.basename(path)
  return filename