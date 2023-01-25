import math
import pandas as pd
import time
from concurrent.futures import ProcessPoolExecutor 

class Chunks:
    def __init__(self, df_path, col):
        self.df = pd.read_csv(df_path)
        self.col = self.df[col]

    def make_chunks(self, num_chunks):
        num_rows = self.df.shape[0]
        chunk_size = math.ceil(num_rows / num_chunks)

        chunks = []
        for i in range(0, num_rows, chunk_size):
            chunk = self.df[i:i + chunk_size]
            chunks.append(chunk)
        
        return chunks

    def count_col(self):
        count_dict = {}
        for each in self.col.unique():
            col_count = self.col.str.count(each).sum()
            count_dict[each]=col_count
        return count_dict

    def processes(self, num_chunks):
        with ProcessPoolExecutor() as exe:
            processes = [exe.submit(self.count_col) for chunk in self.make_chunks(num_chunks)]
        results = [process.result() for process in processes]
        merged_results = {}
        for result in results:
            for each in set(result):
                merged_results[each] = merged_results.get(each, 0) + result.get(each, 0)
        print(merged_results)

if __name__ == "__main__":
    top_richest = Chunks('parallel processing\Lesson3\TopRichestInWorld.csv', 'Industry')
    top_richest.processes(6)

