import os

import yaml

from Base.readData import GetData

with open("./Data" + os.sep + "search_data.yml", "r", encoding="utf-8")as f:
    data_list = []
    data = GetData.get_yaml_data("search_data.yml")
    for i in data.values():
        print((i.get("input_data"), (i.get("expect_data"))))
