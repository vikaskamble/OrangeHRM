import configparser
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
config = configparser.ConfigParser()
import unittest
from POMProjectDemo.Pages.LoginPage import LoginPage
from pyunitreport import HTMLTestRunner
from os.path import dirname, abspath


class GetConfig:

    def getConfig(self, sections, getVal):

        try:
            dir = os.getcwd()
            # print(dir)
            # d = dirname(dirname(dirname(abspath(__file__))))
            d = dirname(dirname(abspath(__file__)))+"\config.conf"
            # print("Test Path", d)

            config.read("C:/Users/vikas.k/PycharmProjects/UIAutomationFrameWork/config.conf")
            # print(config.sections())
            # print(config[sections][getVal])
            return config[sections][getVal]
        except:
            print("Read Config error.")

# config.read("C:/Users/vikas.k/PycharmProjects/UIAutomationFrameWork/config.conf")
# print(config.sections())
# print(config['BROWSER']['browser1'])