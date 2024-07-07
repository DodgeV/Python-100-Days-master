import threading  
import random  
import time  
from queue import Queue  

gmoney = 1000  # 初始金币  
glock = threading.Lock()  
gtotaltimes = 10  # 次数
gTimes = 0  

class Producer(threading.Thread):  
    def run(self):  
        global gmoney, gTimes  
        while True:  
            money = random.randint(100, 1000)  
            with glock:  
                gmoney += money  
                gTimes += 1  
                print(f'赚了{money} 总共{gmoney}')  
                if gTimes >= gtotaltimes:  
                    break  
            time.sleep(0.5)  

def creatproducer():  
    for x in range(5):  
        t = Producer(name=f'producer {x}')  
        t.start()  

def main():  
    creatproducer()  
    # 等待所有生产者线程完成  
    for t in threading.enumerate():  
        if t.name.startswith('producer'):  
            t.join()  
    print(f'最终总金额: {gmoney}')  

if __name__ == '__main__':  
    main()
