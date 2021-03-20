import os
from constants import constant

_CUR_PATH = os.path.abspath(os.path.dirname(__file__))


class Util(object):
    @staticmethod
    def get_root_path():
        return _CUR_PATH[:_CUR_PATH.find(f"{constant.PROJECT_NAME}") + len(f"{constant.PROJECT_NAME}")]
