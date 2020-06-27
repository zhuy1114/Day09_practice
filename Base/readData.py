import os

import yaml


class GetData:
    @classmethod
    def get_yaml_data(cls, name):
        with open("./Data" + os.sep + name, "r", encoding="utf-8")as f:
            return yaml.safe_load(f)
