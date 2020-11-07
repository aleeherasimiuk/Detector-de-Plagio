import matplotlib.pyplot as plt

def show_bar_graphic(dictionary, xlabel, ylabel):
  plt.figure(figsize=(25,15))
  plt.bar(range(len(dictionary)), list(dictionary.values()), color='darkturquoise')
  plt.xticks(range(len(dictionary)), list(dictionary.keys()))
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)

