import os
import toml
from utils.util import Util

_ETC_DIR = os.path.join(Util.get_root_path(), 'etc')


class Config(object):
    def __init__(self):
        self.__etc_file = os.path.join(_ETC_DIR, 'financial_report.toml')
        self.__src_data_dir = None

    def init(self):
        try:
            with open(self.__etc_file, 'r') as f:
                data = toml.load(f)
                self.__src_data_dir = os.path.join(Util.get_root_path(), data["report"]["default_src_path"])
        except IOError as e:
            raise e

    @property
    def src_data_dir(self):
        return self.__src_data_dir
