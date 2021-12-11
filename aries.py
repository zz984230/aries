from configs.config import Config
from presenter.shower.dash_app import *
from presenter.shower.global_pt import GlobalPt
from usecase.balance.balance_uc import BalanceUc
from usecase.valuation.valuation_uc import ValuationUc
from usecase.valuation.cloud_uc import CloudUc
from presenter.shower.balance_pt import BalancePt
from presenter.shower.valuation_pt import ValuationPt
from presenter.shower.cloud_pt import CloudPt
import fire


class Program(object):
    def __init__(self):
        self.__cfg = Config()

    def __init(self):
        self.__cfg.init()
        balance_pt = BalancePt()
        valuation_pt = ValuationPt()
        cloud_pt = CloudPt()

        self.__global_pt = GlobalPt(self.__cfg.logo_file, self.__cfg.bg_file, balance_pt, valuation_pt, cloud_pt).set_global_layout().set_left_layout().render()

        self.__balance_uc = BalanceUc(self.__cfg, balance_pt)
        self.__valuation_uc = ValuationUc(valuation_pt)
        self.__cloud_uc = CloudUc(cloud_pt)

    def start(self):
        self.__init()
        print("Good")
        self.__balance_uc.run()
        self.__valuation_uc.run()
        self.__cloud_uc.run()
        render()
        app.run_server(debug=True)


if __name__ == "__main__":
    fire.Fire(Program)
