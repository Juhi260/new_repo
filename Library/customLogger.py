import logging

class LogGen:
    print("yes")
    @staticmethod
    def loggen():
        print("checking")
        logging.basicConfig(filename=r"C:\Users\juhis\PycharmProjects\FlipkartProject\Logs\automation.log",format='%(asctime)s: %(levelname)s %(message)s',datefmt='%m/%d/%y,%I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

