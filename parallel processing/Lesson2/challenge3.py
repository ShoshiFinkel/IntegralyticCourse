import multiprocessing

class Vault:
    def __init__(self):
        self.total = {}
    
    def create_account(self, account_number):
        self.total[account_number]= 0

    def add_money(self, sum, account_number, shared_value):
        self.total[account_number] += sum
        with shared_value.get_lock():
            shared_value.value += self.total
        return

    def total(self, shared_value):
        sumtotal = 0
        for account in self.total.values():
            sumtotal += account
        with shared_value.get_lock():
            shared_value.value += sumtotal
        return

if __name__ == '__main__':
    shared_value = multiprocessing.Value('i')
    vault = Vault()
    p1 = multiprocessing.Process(target= vault.create_account, args=[123456])
    p2 = multiprocessing.Process(target= vault.create_account, args=[2468])
    p3 = multiprocessing.Process(target= vault.create_account, args=[98765])
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    p4 = multiprocessing.Process(target= vault.add_money, args=[500.5, 123456, shared_value])
    p5 = multiprocessing.Process(target= vault.add_money, args=[763, 2468, shared_value])
    p6 = multiprocessing.Process(target= vault.add_money, args=[180.75, 98765, shared_value])
    p4.start()
    p5.start()
    p6.start()
    p4.join()
    p5.join()
    p6.join()
    p7 = multiprocessing.Process(target= vault.total, args=[shared_value])

    #I didn't find the problem with the add_money function:(
            

