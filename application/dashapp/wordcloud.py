import os

from os import path
from wordcloud import WordCloud, STOPWORDS

import numpy as np
import matplotlib.pyplot as plt
import chart_studio.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
import dash_core_components as dcc

def generate_worldcloud():
    # Read the whole text.
    text = open('application/static/data/Messages.txt', encoding="utf-8-sig").read()

    # Generate a word cloud image
    stopwords = open("application/static/data/stopwords-de.txt", encoding="utf8").read().split()
    # print(stopwords)
    blacklist = STOPWORDS.union(set(stopwords))
    wordcloud = WordCloud(width=800, height=400, stopwords=blacklist, background_color="white").generate(text)

    # Display the generated image:
    # the matplotlib way:

    mpl_fig, ax = plt.subplots()

    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    mpl_fig.savefig('application/static/data/wordcloud.png', dpi=800)
  
