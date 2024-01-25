import pandas as pd
from pandas.api.types import is_numeric_dtype

df = pd.read_csv('../data/combined_df_2023.csv', index_col = 0)

ladder_sorted_df = df.sort_values(by=['Ladder score'], ascending=False)
top_10_countries = ladder_sorted_df.head(10)
bottom_10_countries = ladder_sorted_df.tail(10)

grouped_regions = df.groupby(by=['Regional Indicator'], as_index=False)

numeric_cols = []
non_numeric_cols = []

for col in df.columns:
    if is_numeric_dtype(df[col]):
        numeric_cols.append(col)
    else:
        non_numeric_cols.append(col)   

grouped_regions_mean = grouped_regions[[*numeric_cols]].mean()
grouped_regions_mean.sort_values(by="Ladder score", inplace=True, ascending=False)


df_columns = list(df.columns)
except_columns = ['Ladder score standard error',
       'Ladder score upper whisker', 'Ladder score lower whisker',
        'Regional Indicator']
# columns for metric graphs
metric_graph_columns = [col for col in df_columns if col not in except_columns]


# add iso codes
iso_df = pd.read_csv('../data/world_countries_with_sectors.csv')
iso_df_to_merge = iso_df[['Country', 'Code']]
df_with_iso = df.merge(iso_df_to_merge, how='left', on='Country')

