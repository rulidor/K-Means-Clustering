import kit as kit
import learn as learn
import pandas as pd
import numpy as np
# import matplotlib as plt
import matplotlib.pyplot as plt

import statistics as stats
import sklearn
import plotly.graph_objects as go
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pycountry

class Preprocessing:
    def __init__(self):
        self.df = None
        self.grouped_df = None

    def load_dataset_to_df(self, path):
        try:
            self.df = pd.read_excel(path)
            return True
        except Exception as e:
            return False

    def pre_process(self):
        if self.df is None:
            return False
        df = self.df
        for column in df.columns:
            if column != "country" and column != "year":
                df[column].fillna(df[column].mean(), inplace=True)
            elif column == "year":
                df[column].fillna(int(df[column].mean()), inplace=True)

        for column in df.columns:
            if column != "country":
                df[column] = (df[column] - df[column].mean()) / df[column].std()

        grouped_df = df.groupby("country").mean()
        del grouped_df['year']
        self.df = df
        self.grouped_df = grouped_df
        return True

    def get_grouped_df(self):
        return self.grouped_df
