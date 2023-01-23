import multiprocessing

def product(num1, num2, shared_value):
    with shared_value.get_lock():
        shared_value.value += num1 * num2

if __name__ == "__main__":
    shared_value = multiprocessing.Value("i")
    p1 = multiprocessing.Process(target=product, args=[4, 5, shared_value])
    p2 = multiprocessing.Process(target=product, args=[3, 6, shared_value])
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(shared_value.value)
