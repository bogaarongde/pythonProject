class Subject:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def unregister_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)

class Observer:
    def update(self, subject):
        pass

class ConcreteObserver(Observer):
    def update(self, subject):
        print("ConcreteObserver: Reagáltam a változásra.")

# Használat
subject = Subject()
observer = ConcreteObserver()
subject.register_observer(observer)
subject.notify_observers()  # Értesíti a megfigyelőt a változásról
