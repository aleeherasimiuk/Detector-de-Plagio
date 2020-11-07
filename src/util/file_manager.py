import os
import filetype

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

def is_rtf(path):
  kind = filetype.guess(path)
  return kind and kind.extension == 'rtf'

def get_filename(path):
  filename = os.path.basename(path)
  return filename

def delete_file(path):
  os.remove(path)