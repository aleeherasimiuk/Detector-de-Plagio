from gensim.models import KeyedVectors
import numpy as np
from repository.csv_tools import get_documents
from models.naive_bayes_utils import NaiveBayes
from models.lda_utils import get_topic_keywords
from document import Document
from nltk import word_tokenize
import util.file_manager as fm
import click
import util.prompt_utils as prompt
import threading
import time
from multiprocessing import Process

documents = []
scrapped = []
books = []

questions = [
    'concepto conducta adaptativo complejas sistema ascendente sistema',
    'sistema emergente autoorganizativo sistema evolutivo caos',
    'desarrollar idea concepto conducta adaptativo complejas sistema ascendente sistema',
    'particular conducta dictiostellum implicancias',
    'enuncie idea componente basa dar ejemplo cada',
    'enunciar ley coase originalmente ahora implicancias',
    'poder caracterizar industrial decir rifkin invento cada infraestructura cada etapa',
    'lectura rifkin clase actual elegir apellido brevemente',
    'pc activo diferencia envolver usuario conducta tipo problema naturaleza interactivo pc distinguir individuo educados poder orientados manejo ser trabajador conocimiento analista conceptuales',
    'definir caracterizar experiencia diferencia producto servicio',
    'ejemplo distinto real si conocer invente experiencia',
    'mismo aproximadamente porcentaje fin respecto usuario',
    'relacionar ley pareto masa largo cola',
    'dar ejemplo internacional empresa producto servicio modelo largo cola'
  ]

def color_print(text, color):
  click.echo(click.style(text, fg=color))

def get_color(n):
  if n == 0:
    return 'red'
  if n <= 1:
    return 'yellow'
  return 'green'

def is_useful(topic, document):
  return document.topic == topic

def is_useful_text(lemmatized_string, original_string):
  return lemmatized_string not in questions and len(word_tokenize(lemmatized_string)) > 5 and '?' not in original_string and '¿' not in original_string

def is_pdf(document):
  return fm.is_pdf(document.title)

def loading():
  t = Process(target=prompt.animate)
  t.start()
  
  #t = threading.Thread(target=prompt.animate)
  #t.daemon=True
  #t.start()

  return t

def process_document(path):
  return Document(path=path, preprocess_list= ['lemmatized_string', 'sentences', 'preprocessed_sentences', 'paragraphs', 'preprocessed_paragraphs', 'named_entities', 'urls'])

def fetch_documents(scrap, book):
  global documents
  global scrapped
  global books
  documents = get_documents('data/dataset.csv')

  if scrap:
    scrapped = get_documents('data/scrapped.csv')
  
  if book:
    books = get_documents('data/books.csv')


def classificate(document):
  classifier = NaiveBayes()
  classifier.load_model(path='data/')
  acc = classifier.accuracy

  topic, _ = classifier.topic(document.lemmatized_string)

  keywords, p = get_topic_keywords(document.lemmatized_string, path='data/lda_model')

  return (topic, acc, keywords, p)


def filter_documents(scrap, book, topic, keywords):
  
  filtered_documents = [document for document in documents if is_useful(topic, document)]
  filtered_web_texts = []
  filtered_books = []
  if scrap:
    filtered_web_texts = [document for document in scrapped if is_useful(keywords, document)]
  
  if book:
    filtered_books = [book for book in books if is_useful(topic, book)]

  return filtered_documents, filtered_web_texts, filtered_books


def evaluate(doc_eval, word_vectors, filtered_documents, filtered_web_texts, filtered_books):
  treshold = 1.65

  paragraphs = []
  sentences = []
  paragraph_count = len(doc_eval.preprocessed_paragraphs)
  sentence_count = len(doc_eval.preprocessed_sentences)

  for document in filtered_documents:
    if is_pdf(document) or is_pdf(doc_eval):
      for i, sentence in enumerate(doc_eval.preprocessed_sentences):
        for j, other_sentence in enumerate(document.preprocessed_sentences):
          if is_useful_text(sentence, doc_eval.sentences[i]):
            distance = word_vectors.wmdistance(sentence, other_sentence)
            if distance <= treshold:
              sentences.append(
                (document, i, j, distance)
              )
    else:
      for i, paragraph in enumerate(doc_eval.preprocessed_paragraphs):
        for j, other_paragraph in enumerate(document.preprocessed_paragraphs):
          if is_useful_text(paragraph, doc_eval.paragraphs[i]):
            distance = word_vectors.wmdistance(paragraph, other_paragraph)
            if distance <= treshold:
              paragraphs.append(
                (document, i, j, distance)
              )

  for scrapped in filtered_web_texts:
    for i, paragraph in enumerate(scrapped.preprocessed_paragraphs):
      for j, other_paragraph in enumerate(doc_eval.preprocessed_paragraphs):
        distance = word_vectors.wmdistance(paragraph, other_paragraph)
        if distance <= treshold:
          paragraphs.append(
            (scrapped, j, i, distance)
          )


  for book in filtered_books:
    for i, sentence in enumerate(book.preprocessed_sentences):
      for j, other_sentence in enumerate(doc_eval.preprocessed_sentences):
        distance = word_vectors.wmdistance(sentence, other_sentence)
        if distance <= treshold:
          sentences.append(
            (book, j, i, distance)
          )

  paragraphs_percentage = (len(paragraphs) * 100) / paragraph_count
  sentences_percentage = (len(sentences) * 100) / sentence_count

  final_percentage = paragraphs_percentage + sentences_percentage

  return paragraphs, sentences, paragraph_count, sentence_count, round(final_percentage, 2)


@click.command()
@click.option('--path', help='Path del documento a evaluar.')
@click.option('--scrap', is_flag=True, prompt='¿Desea scrappear la web en busca de plagio?')
@click.option('--book', is_flag=True, prompt='¿Desea comparar con otros libros en busca de plagio?')
def hello(path, scrap, book):
  click.clear()

  click.echo('Procesando documento: {}'.format(path))
  t = loading()
  document_to_evaluate = process_document(path)
  prompt.finish('Listo!')
  t.terminate()
  time.sleep(0.5)
  click.clear()
  
  click.echo('Obteniendo documentos para comparar')
  t = loading()
  fetch_documents(scrap, book)
  prompt.finish('Listo!')
  t.terminate()
  time.sleep(0.5)
  click.clear()

  click.clear()
  click.echo('Documentos para analizar:\n')
  click.echo('\tDocumentos: {}'.format(len(documents)))
  if scrap:
    click.echo('\tWebs scrappeadas: {}'.format(len(scrapped)))
  if book:
    click.echo('\tLibros: {}'.format(len(books)))


  click.echo('Analizando el tema del texto:\n')
  topic, accuracy, keywords, p = classificate(document_to_evaluate)

  click.echo('Naive Bayes -> {}  [{}% de efectividad]\n'.format(topic, round(accuracy, 2)))
  click.echo('Latent Dirichlet Allocation -> [{}] -> [probabilidad del {}%]'.format(keywords, round(p*100,2)))


  click.echo('\nFiltrando documentos por tema...\n')

  filtered_documents, filtered_scrapped, filtered_books = filter_documents(scrap, book, topic, keywords)

  click.echo('\tDocumentos a analizar: {}'.format(len(filtered_documents)))

  if scrap:
    click.echo('\tTextos scrappeados a analizar: {}'.format(len(filtered_scrapped)))

  if book:
    click.echo('\tLibros a analizar: {}'.format(len(filtered_books)))


  click.echo('\nPresione una tecla para comenzar con el análisis de plagio.')
  click.pause()

  click.clear()
  click.echo('Iniciando modelo de Word Embeddings')
  t = loading()
  word_vectors = KeyedVectors.load('keyed_vectors/complete.kv')
  prompt.finish('Listo!')
  t.terminate()
  time.sleep(0.5)
  click.clear()

  click.echo('Analizando plagio')
  t = loading()
  paragraphs, sentences, paragraph_count, sentence_count, final_percentage = evaluate(document_to_evaluate, word_vectors, filtered_documents, filtered_scrapped, filtered_books)
  prompt.finish('Listo!')
  t.terminate()
  time.sleep(0.5)
  click.clear()

  if final_percentage < 30:
    click.echo('No se ha detectado plagio ({}%)'.format(final_percentage))
    exit()

  click.echo('Porcentaje de plagio: {}%'.format(final_percentage))
  

  for document, index_eval, index_doc, distance in paragraphs:
    color = get_color(distance)
    color_print('-'*150, color)
    color_print('Párrafo plagio: [Párrafo #{}]'.format(index_eval), color)
    color_print(document_to_evaluate.paragraphs[index_eval], color)
    color_print('\n\n', color)
    color_print('Párrafo de referencia: [{}][Párrafo #{}]'.format(document.title, index_doc), color)
    color_print(document.paragraphs[index_doc], color)

    color_print('\n\nDistancia: {}'.format(distance), color)
    color_print('-'*150, color)


  for document, index_eval, index_doc, distance in sentences:
    color = get_color(distance)
    color_print('-'*150, color)
    color_print('Oración plagio [Oración #{}]'.format(index_eval), color)
    color_print(document_to_evaluate.sentences[index_eval], color)
    color_print('\n\n', color)
    color_print('Oración de referencia: [{}][Oración #{}]'.format(document.title, index_doc), color)
    color_print(document.sentences[index_doc], color)

    color_print('\n\nDistancia: {}'.format(distance), color)
    color_print('-'*150, color)

if __name__ == '__main__':
  hello()