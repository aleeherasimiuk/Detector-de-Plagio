from gensim.models import LdaMulticore
model = None

def get_lda_model(path = '../data/lda_model'):
  model = LdaMulticore.load(path)
  return model

def get_keywords(path = '../data/lda_model'):
  m = model if model else get_lda_model(path)
  return [topic_names(topic) for p, topic in m.show_topics(-1, formatted = False)]

def get_topic_names(topic):
    t, _ = topic
    return t

def topic_names(topic):
  return ' '.join(list(map(get_topic_names, topic)))

