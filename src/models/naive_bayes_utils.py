import random

def split_dataset(docs, test_size):
    random.shuffle(docs)

    test = int(len(docs) * test_size)
    texts_train = [doc[0] for doc in docs[test:]]
    topic_train = [doc[1] for doc in docs[test:]]
    texts_test  = [doc[0] for doc in docs[:test]]
    topic_test  = [doc[1] for doc in docs[:test]]

    return texts_train, topic_train, texts_test, topic_test

def get_documents_from_class(texts, classes, topic):
    return [texts[index] for index, classname in enumerate(classes) if classname == topic]

def get_words(vectorizer):
    return vectorizer.get_feature_names(); 

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
        probability = get_word_probability(word, topic, frequencies, total_features, features_by_class)
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