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

class KMeans_Calc:
    def __init__(self):
        self.grouped_df = None

    def calc_k_means(self, grouped_df, n_clusters, n_init):
        if n_clusters <= 0 or n_init <= 0 or n_clusters > grouped_df.shape[0] or isinstance(n_clusters, int) is False or isinstance(n_init, int) is False:
            return "Error: invalid number of clusters or number of runs."
        kmeans = KMeans(n_clusters=n_clusters, n_init=n_init).fit(grouped_df)

        clusters_df = pd.DataFrame(kmeans.labels_, columns=['cluster'])

        grouped_df.insert(loc=14, column='cluster', value=clusters_df)
        self.grouped_df = grouped_df
        grouped_df.to_excel('dataset_with_cluster.xlsx')
        return "Success"

    def plot_scatter(self):
        # colors = np.array([0, 1])
        grouped_df = self.grouped_df

        plt.scatter(grouped_df['Social support'], grouped_df['Generosity'], c=grouped_df['cluster'])

        # df.plot(kind='scatter', x='Social support', y='Generosity')
        plt.colorbar()
        plt.title("K Means Clustering")
        plt.xlabel("Social support")
        plt.ylabel("Generosity")

        # plt.show()
        grouped_df['country'] = grouped_df.index

        # df = px.data.gapminder().query("year==2007")
        countries = {}
        for country in pycountry.countries:
            countries[country.name] = country.alpha_3

        codes = list()
        for c in grouped_df["country"]:
            flag = 0
            for country in countries.keys():
                if c in country:
                    codes.append(countries.get(country, 'Unknown code'))
                    flag = 1
                    break
            if flag == 0:
                codes.append(countries.get(country, '******'))

        # codes = [countries.get(country, 'Unknown code') for country in grouped_df["country"]]
        grouped_df.insert(loc=15, column='iso_alpha', value=codes)

        fig = px.choropleth(grouped_df, locations="iso_alpha",
                            color="cluster", # lifeExp is a column of gapminder
                            hover_name="country", # column to add to hover information
                            color_continuous_scale=px.colors.sequential.Bluered)
        # fig.show()
        fig.update_layout(title_text = 'K Means Clustering Visualization', title_x=0.5)
        return plt, fig



# print("hi")
