import os
import toml
from utils.util import Util

_ETC_DIR = os.path.join(Util.get_root_path(), 'etc')


class Config(object):
    def __init__(self):
        self.__etc_file = os.path.join(_ETC_DIR, 'financial_report.toml')
        self.__src_data_dir = None
        self.__logo_file = None

    def init(self):
        root_path = Util.get_root_path()
        try:
            with open(self.__etc_file, 'r') as f:
                data = toml.load(f)
                self.__src_data_dir = os.path.join(root_path, data["report"]["default_src_path"])
                self.__logo_file = data["icon"]["logo_file"]
        except IOError as e:
            raise e

    @property
    def src_data_dir(self):
        return self.__src_data_dir

    @property
    def logo_file(self):
        return self.__logo_file
