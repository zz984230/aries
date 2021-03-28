from configs.config import Config
from presenter.dash_app import *
from presenter.global_pt import GlobalPt
from usecase.balance.balance_uc import BalanceUc
from presenter.balance_pt import BalancePt
import fire


class Program(object):
    def __init__(self):
        self.__cfg = Config()

    def __init(self):
        self.__cfg.init()
        self.__global_pt = GlobalPt().set_global_layout().set_left_layout().render()
        self.__balance_uc = BalanceUc(self.__cfg, BalancePt(self.__global_pt.get_right_div()))

    def start(self):
        self.__init()
        print("Good")
        self.__balance_uc.run()
        render()
        app.run_server(debug=True)


if __name__ == "__main__":
    fire.Fire(Program)
