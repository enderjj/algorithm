import threading

lock = threading.Lock() # 创建锁

class Singleton:
    instance = None

    def __new__(self):
        if Singleton.instance == None:
            lock.acquire() # 获取锁
            if Singleton.instance == None:
                Singleton.instance = object()
            lock.release() # 释放锁
        return Singleton.instance

single = Singleton()
single1 = Singleton()
print(id(single))
print(id(single1))
