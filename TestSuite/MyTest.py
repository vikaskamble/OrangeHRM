import os
import configparser
config = configparser.ConfigParser()

dir = os.getcwd()
print(dir)

config.read("C:/Users/vikas.k/PycharmProjects/UIAutomationFrameWork/config.conf")
print(config.sections())
print(config['BROWSER']['browser'])
