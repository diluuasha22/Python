from abc import abstractmethod
class Log:
    @abstractmethod
    def debug(self, text: str):
        print("debug: " + text)

    @abstractmethod
    def info(self, text: str):
        print("info: " + text)

    @abstractmethod
    def warn(self, text: str):
        print("warn: " + text)

    @abstractmethod
    def error(self, text: str):
        print("error: " + text)

    @abstractmethod
    def crit(self, text: str):
        print("crit: " + text)


class ConsoleLog(Log):
    def debug(self, text: str):
        print("\033[32m {}".format(text))

    def info(self, text: str):
        print("\033[34m {}" .format(text))

    def warn(self, text: str):
        print("\033[37m {}" .format(text))

    def error(self, text: str):
        print("\033[31m {}" .format(text))

    def crit(self, text: str):
        print("\033[33m {}" .format(text))


log = ConsoleLog()
log.debug("Дебаг")
log.info("Полезная информация")
log.warn("Предупреждение!")
log.error("Ошибка!")
log.crit("Критическая ошибка!")