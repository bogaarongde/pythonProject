import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        cls._lock.acquire()  # Megszerezzük a zárat a kritikus szakasz elején
        try:
            if not cls._instance:
                cls._instance = super().__new__(cls)
        finally:
            cls._lock.release()  # Felszabadítjuk a zárat a kritikus szakasz végén
        return cls._instance


s1 = ThreadSafeSingleton()
s2 = ThreadSafeSingleton()

print(s1 is s2)  # Output: True