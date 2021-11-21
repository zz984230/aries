from repository.cloud_repo import CloudSheet


class CloudUc(object):
    def __init__(self, prt):
        self.__repo = CloudSheet()
        self.__prt = prt

    def __deal_data(self):
        pass

    def run(self):
        self.__deal_data()
        self.__prt.render(self.__repo)
