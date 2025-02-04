#first we have to import configparser,
#using configparser we call the method RawConfigParser
#and create object of that,then call read method ,pass path of config file
#create a class,and for every data we have to create separate method,
#using object we call get method,and we will pass the header of info and key of that
#then we make it as static
import configparser
config=configparser.RawConfigParser()
config.read("C:\\Users\juhis\PycharmProjects\FlipkartProject\configurations\config.ini")

class ReadConfig:
    @staticmethod
    def getUrl():
        url=config.get("common data","Base_url")
        return url

    @staticmethod
    def getEmail():
        email=config.get("credentials","email")
        return email

    @staticmethod
    def getPassword():
        pwd=config.get("credentials","password")
        return pwd


