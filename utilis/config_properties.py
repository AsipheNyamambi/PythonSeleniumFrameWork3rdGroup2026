import concurrent
import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/commonDetails.ini")

class ReadConfig_CommonDetails():
    def getDevUrl(self):
        return config.get("server connection","dev_url")

    def getUsername(self):
        return config.get("server connection","test_url")



