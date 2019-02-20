import configparser
import os

config = configparser.ConfigParser()
config.read("panda-config.ini")

config.add_section("mobile")
config.set("mobile","deviceName","5422097f")
config.set("mobile","platformVersion","platformVersion")

config.write(open("panda-config.ini", "w"))


'''
读取
config.read("panda-config.ini")
xxx = config.get('mobile','deviceName')
'''
