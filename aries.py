from configs.config import Config
import fire


class Server(object):
    def __init__(self):
        self.__cfg = Config()
        self.__init_config()

    def __init_config(self):
        self.__cfg.init()

    def start(self):
        print("Good")


if __name__ == "__main__":
    fire.Fire(Server)
