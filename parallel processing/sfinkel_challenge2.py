import time
import multiprocessing

tasks = ['wash the dishes', 'bake a cake', 'fold the laundry', 'iron the shirts', 'sweep the bedroom', 'buy milk', 'wash the floor', 'bath the kids', 'buy bread', 'buy sugar']

def run_task(your_list):
    print(your_list)
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=run_task, args=[tasks[:2]])
    p2 = multiprocessing.Process(target=run_task, args=[tasks[3:7]])
    p3 = multiprocessing.Process(target=run_task, args=[tasks[7:]])
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p2.join()




