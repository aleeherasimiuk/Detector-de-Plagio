from matplotlib import pyplot as plt
from wordcloud import WordCloud
import matplotlib.colors as mcolors
from util.data_cleaning import stop_words


def show_word_cloud(model, rows, columns):
  
  cols = [color for name, color in mcolors.TABLEAU_COLORS.items()] * 2

  cloud = WordCloud(stopwords=stop_words(),
                    background_color='white',
                    width=2500,
                    height=3000,
                    max_words=10,
                    colormap='tab10',
                    color_func=lambda *args, **kwargs: cols[i],
                    prefer_horizontal=1.0)

  topics = model.show_topics(num_topics = -1, formatted=False)

  fig, axes = plt.subplots(rows, columns, figsize=(20, 10), sharex=True, sharey=True)

  for i, ax in enumerate(axes.flatten()):
    fig.add_subplot(ax)
    topic_words = dict(topics[i][1])
    cloud.generate_from_frequencies(topic_words, max_font_size=300)
    plt.gca().imshow(cloud)
    plt.gca().set_title('Topic ' + str(i), fontdict=dict(size=16))
    plt.gca().axis('off')


  plt.subplots_adjust(wspace=0, hspace=0)
  plt.axis('off')
  plt.margins(x=0, y=0)
  plt.tight_layout()
  plt.show()
