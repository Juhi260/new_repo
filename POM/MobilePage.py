from Library.genericUtilities import SeleniumWrapper
from POM.HomePage import HomePage



class MobilePage(HomePage):
    _oppo=("xpath","//img[@alt='POCO C61 (Diamond Dust Black, 64 GB)']")


    def oppo(self):
        self.click_item(self._oppo)
