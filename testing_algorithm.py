# -*- coding: utf-8 -*-
"""testing_algorithm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UVTlDqqtek4L-Ja10xU0HtWyTIqU6xlG
"""

from google.colab import files
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# files.upload()
dataset = pd.read_csv('testing_algorithm.csv')
dataset = dataset.drop(columns=['time_online_per_week', 'times_asked_for_help_per_week', 'time_spent_on_assignment'])
print(np.mean(abs(dataset['predicted_score'] - dataset['actual_score'])))
from pandas.plotting import table # EDIT: see deprecation warnings below
dataset['difference'] = abs(dataset['predicted_score'] - dataset['actual_score'])
display(dataset)
import six

df = pd.DataFrame()


def render_mpl_table(data, col_width=3.0, row_height=0.625, font_size=14,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in  six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    return ax

render_mpl_table(dataset, header_columns=0, col_width=3.0)