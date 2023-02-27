import math
import pandas as pd
from multiprocessing import Pool
import functools
def make_chunks(df, num_chunks):
    num_rows = df.shape[0]
    chunk_size = math.ceil(num_rows / num_chunks)
    chunks = []
    for i in range(0, num_rows, chunk_size):
        chunk = df[i:i + chunk_size]
        chunks.append(chunk)
    return chunks
def count_industries(df):
    people_in_industries = {}
    for industry_name in industries:
        people_in_industries[industry_name] = df['Industry'].str.count(industry_name).sum()
    return people_in_industries

df = pd.read_csv('hotel_bookings.csv', na_values = ['undefined', '', 'none', '-'])
data = dict(df['lead_time'].value_counts())
print(data)
# industries = richest_people['Industry'].unique()
# rp_chunks = make_chunks(richest_people, 8)

# if __name__ == "__main__":
#     with Pool(8) as pool:
#         chunk_results = pool.map(count_industries, rp_chunks)
#     for chunk1 in chunk_results:
#         merged = {}
#         merged.update(freq_chunk1)
#         merged.update(freq_chunk2)
#         print(merged)
#     result = functools.reduce(update, chunk_results)
#     print(chunk_results)
   