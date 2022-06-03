

import json


class StorageManager:
    def get_filename(self, data_name):
        return data_name + ".json"
    def load_data(self, data_name):
        try:
            filname = self.get_filename(data_name)
            file = open(filname, "r")
            data = file.read()
        except:
            return None

        file.close()
        return json.loads(data)

    def save_data(self, data_name, data_content):
        filname = self.get_filename(data_name)
        data_str = json.dumps(data_content)
        file = open(filname, "w")
        data = file.write(data_str)

        file.close()
