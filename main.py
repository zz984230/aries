from configs.config import Config


class Server(object):
    def __init__(self):
        self.__cfg = Config()

    def __init_config(self):
        self.__cfg.init()

    def init(self):
        self.__init_config()

    def start(self):
        pass


if __name__ == "__main__":
    s = Server()
    s.init()
    s.start()
