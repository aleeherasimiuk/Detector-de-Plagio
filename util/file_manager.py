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