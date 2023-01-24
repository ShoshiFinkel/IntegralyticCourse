import pandas as pd
df = pd.read_csv('parallel processing\Lesson3\TopRichestInWorld.csv')

working_in_tech = df['Industry'].str.count('Technology').sum()
industries = {}
industries['Technology'] = working_in_tech

