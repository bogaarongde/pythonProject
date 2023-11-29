class Subject:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def unregister_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self,inputtext):
        for observer in self._observers:
            observer.update(inputtext)

class Observer:
    def update(self, inputtext):
        pass

class ConcreteObserver(Observer):
    def update(self, inputtext):
        print(f"ConcreteObserver: Reagáltam a változásra.{inputtext}")

class ConcreteObserver2(Observer):
    def update(self, inputtext):
        print(f"ConcreteObserver2: Reagáltam a változásra.{inputtext}")

# Használat
subject = Subject()
observer = ConcreteObserver()
observer2 = ConcreteObserver2()
subject.register_observer(observer)
subject.register_observer(observer2)
subject.notify_observers("test")  # Értesíti a megfigyelőt a változásról
