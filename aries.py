from configs.config import Config
from presenter.dash_app import *
from usecase.balance.balance_uc import BalanceUc
from presenter.balance_pt import BalancePt
import fire


class Program(object):
    def __init__(self):
        self.__cfg = Config()

    def __init(self):
        self.__cfg.init()
        self.__balance_uc = BalanceUc(self.__cfg, BalancePt())

    def start(self):
        self.__init()
        print("Good")
        self.__balance_uc.run()
        app.run_server(debug=True)


if __name__ == "__main__":
    fire.Fire(Program)
