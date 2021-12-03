import csv
import pandas as pd
import matplotlib.pyplot as plt
# from scipy import stats


def plot_smell_dist(df):
  smell_types = df['type'].value_counts()
  # plt.bar(smell_types.index, smell_types.values)
  plt.pie(smell_types, labels=smell_types.keys(), autopct='%1.1f%%')
  plt.show()

def read_csv(filename):
  df = pd.read_csv(filename)
  df['year'] = df['year'].astype(str).str[:4]
  return df

def main():
  # distribution of DL vs SC smell types
  # df = read_csv("./results/smells_filtered.csv")
  # plot_smell_dist(df)

  # Top smells
  # df = read_csv("./results/smells_filtered.csv")
  # tmp = df['smell_code'].value_counts()
  # print(tmp.head(10))

  # DL vs SC smell types over time (years; sampled data, 1300 projects per each year)
  # df = read_csv("./results/samples/year_filtered.csv")
  # tmp = df.groupby(['type', 'year'])['type'].count()
  # print(tmp.head(20))

  # Number of smells per year
  # df = read_csv("./results/samples/year_filtered.csv")
  # tmp = df['year'].value_counts()
  # print(tmp.head(20))

  # Number of smells by owner type (sampled data, 14000 projects per each owner type)
  # df = read_csv("./results/samples/owner_filtered.csv")
  # tmp = df['owner_type'].value_counts()
  # print(tmp.head())

  # Number of smells by language (sampled data, 330 projects per each language)
  # df = read_csv("./results/samples/language_filtered.csv")
  # tmp = df['language'].value_counts()
  # print(tmp.head(20))

  # Number of smells by language (sampled data, 1500 projects per each language)
  # df = read_csv("./results/samples/language2_filtered.csv")
  # tmp = df['language'].value_counts()
  # print(tmp.head(20))
  pass


if __name__ == "__main__":
  main()