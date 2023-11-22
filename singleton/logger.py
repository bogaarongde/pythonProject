class Logger:
    _instance = None
    _log_messages = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def log(self, message):
        self._log_messages.append(message)

    def get_logs(self):
        return self._log_messages


class ClassA:
    def perform_action(self):
        logger = Logger()
        logger.log("ClassA performed an action")


class ClassB:
    def perform_action(self):
        logger = Logger()
        logger.log("ClassB performed an action")


def test():
    obj_a = ClassA()
    obj_b = ClassB()

    obj_a.perform_action()
    obj_b.perform_action()

    logger = Logger()
    logs = logger.get_logs()
    print("Naplózott üzenetek:")
    for message in logs:
        print(message)

if __name__ == "__main__":
    test()