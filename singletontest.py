from singleton.logger import Logger


def dosomething


logger = Logger()
logs = logger.get_logs()
print("Naplózott üzenetek:")
for message in logs:
    print(message)