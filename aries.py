from configs.config import Config
import fire


class Program(object):
    def __init__(self):
        self.__cfg = Config()

    def __init(self):
        self.__cfg.init()

    def start(self):
        self.__init()
        print("Good")


if __name__ == "__main__":
    fire.Fire(Program)
