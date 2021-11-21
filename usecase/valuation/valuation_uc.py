from repository.valuation_repo import ValuationSheet


class ValuationUc(object):
    def __init__(self, prt):
        self.__repo = ValuationSheet('贵州茅台')
        self.__prt = prt

    def __deal_data(self):
        pass

    def run(self):
        self.__deal_data()
        self.__prt.render(self.__repo)
