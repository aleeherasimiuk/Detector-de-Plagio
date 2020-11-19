import random
import pandas as pd
import math


def split_dataset(docs, test_size):
    random.shuffle(docs)

    test = int(len(docs) * test_size)
    texts_train = [doc[0] for doc in docs[test:]]
    topic_train = [doc[1] for doc in docs[test:]]
    texts_test = [doc[0] for doc in docs[:test]]
    topic_test = [doc[1] for doc in docs[:test]]

    return texts_train, topic_train, texts_test, topic_test


def get_documents_from_class(texts, classes, topic):
    return [texts[index] for index, classname in enumerate(classes) if classname == topic]


def get_words(vectorizer):
    return vectorizer.get_feature_names()


def get_words_count(term_document_matrix):
    return term_document_matrix.toarray().sum(axis=0)


def get_frecuencies(word_list, count_list):
    return dict(zip(word_list, count_list))


def get_probabilities(word_list, count_list):
    prob = [(count / len(word_list)) for count in count_list]
    return dict(zip(word_list, prob))


def get_features_count(count_list):
    return count_list.sum(axis=0)


def get_total_features(frequencies, set_of_classes):

  features = []
  for topic in set_of_classes:
    features.extend([key for key in frequencies[topic].keys()])

  return len(set(features))


def get_class_probabilities(classes):
  class_probabilities = {}
  for topic in classes:
    class_probabilities[topic] = classes.count(topic) / len(classes)
  return class_probabilities


def get_word_probability(word, topic, frequencies, total_features, features_by_class):
    freq = frequencies[topic]
    count = freq[word] if word in freq.keys() else 0
    return (count + 1) / (features_by_class[topic] + total_features)


def get_words_probabilities(document, topic, frequencies, total_features, features_by_class):
    prob = []
    for word in document:
        probability = get_word_probability(
            word, topic, frequencies, total_features, features_by_class)
        prob.append(probability)
    return dict(zip(document, prob))


def get_topic_predicted(predicted_probabilities):

    max_probability = None
    topic = None

    for key in predicted_probabilities.keys():
        p = predicted_probabilities[key]
        if not max_probability or p > max_probability:
            max_probability = p
            topic = key

    return topic, max_probability


class NaiveBayes():

  frequencies = None
  classes = None
  features_by_class = None
  class_probabilities = None
  total_features = None
  accuracy = None
  fail_ratio = None

  def init(self, frequencies, classes, features_by_class, class_probabilities):
    self.frequencies = frequencies
    self.classes = classes
    self.features_by_class = features_by_class
    self.class_probabilities = class_probabilities
    self.total_features = get_total_features(self.frequencies, self.classes)

  def save_model(self, path):
    frequencies_to_save = pd.Series(self.frequencies, name='Frequencies')
    classes_to_save = pd.Series(list(self.classes), name='Classes')
    features_by_class_to_save = pd.Series(self.features_by_class, name='Features by Class')
    class_probabilities_to_save = pd.Series(self.class_probabilities, name='Class Probabilities')

    frequencies_to_save.to_csv('{}frequencies.nv'.format(path))
    classes_to_save.to_csv('{}classes.nv'.format(path))
    features_by_class_to_save.to_csv('{}features_by_class.nv'.format(path))
    class_probabilities_to_save.to_csv('{}class_probabilities.nv'.format(path))

  def load_model(self, path):
    self.frequencies = pd.read_csv('{}frequencies.nv'.format(path)).to_list()
    self.classes = pd.read_csv('{}classes.nv'.format(path)).to_list()
    self.features_by_class = pd.read_csv('{}features_by_class.nv'.format(path)).to_list()
    self.class_probabilities = pd.read_csv('{}}class_probabilities.nv'.format(path)).to_list()
    self.accuracy = pd.read_csv('{}accuracy.nv'.format(path)).to_dict()['accuracy']
    self.fail_ratio = pd.read_csv('{}accuracy.nv'.format(path)).to_dict()['failed']

  def topic(self, string):
    predicted_probabilities = {}
    for topic in self.classes:
        words_probability = get_words_probabilities(string, topic, self.frequencies, self.total_features, self.features_by_class)
        P = math.log(self.class_probabilities[topic], 2)
        for key in words_probability.keys():
            p = words_probability[key]
            P += math.log(p, 2)
        predicted_probabilities[topic] = P
    
    topic_predicted, probability_predicted = get_topic_predicted(predicted_probabilities)
    return(topic_predicted, probability_predicted)

  def set_accuracy(self, fiability, path = '../data/'):
    self.accuracy = fiability['accuracy']
    self.fail_ratio = fiability['failed']
    pd.Series(data=fiability).to_csv('accuracy.nv'.format(path))


