import pandas as pd
import math
from multiprocessing import Pool
import functools

df = pd.read_csv('project\hotel_bookings.csv', na_values = ['Undefined', '', 'none', '-'])

def make_chunks(df, num_chunks):
    chunk_size = math.ceil(df.shape[0] / num_chunks)
    return [df[i:i+chunk_size] for i in range(0, df.shape[0], chunk_size)]

def map_reduce(data, num_processes, mapper, reducer):
    chunks = make_chunks(data, num_processes)
    
    with Pool(num_processes) as pool:
        chunk_results = pool.map(mapper, chunks)
    return functools.reduce(reducer, chunk_results)

def mapper(data):
    lead_time_count = dict(data['lead_time'].value_counts())
    num_list = [2,4,6,8,10,12,14,16,18,20]
    result_dict = {}
    for num in num_list:
        if num in lead_time_count:
            result_dict[num]=lead_time_count[num]
    return result_dict

def reducer(freq_chunk1, freq_chunk2):
    for k in set(freq_chunk2):
        freq_chunk1[k]=freq_chunk1.get(k,0) + freq_chunk2.get(k,0)
    return freq_chunk1

if __name__ == '__main__':   
    result = map_reduce(df, 8, mapper, reducer)
    print(result) 
    