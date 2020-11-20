from gensim.models import LdaMulticore
model = None

def get_lda_model(path = '../data/lda_model'):
  model = LdaMulticore.load(path)
  return model

def get_keywords(path = '../data/lda_model'):
  m = model if model else get_lda_model(path)
  return [topic_names(topic) for p, topic in m.show_topics(-1, formatted = False)]

def get_topic_keywords(string, path = '../data/lda_model'):
  m = model if model else get_lda_model(path)
  id2token = m.id2word
  bow = id2token.doc2bow(string)
  result = m[bow]
  return __get_topic(result)

def __get_topic(result):
  
  predicted_topic = None
  probability = 0
  
  for topic, p in result:
    if p > probability:
      predicted_topic = topic
      probability = p

  return get_keywords()[predicted_topic], p


def get_topic_names(topic):
    t, _ = topic
    return t

def topic_names(topic):
  return ' '.join(list(map(get_topic_names, topic)))

