from Library.genericUtilities import SeleniumWrapper
from POM.HomePage import HomePage



class MobilePage(HomePage):
    _oppo=("xpath","//img[@alt='POCO C61 (Diamond Dust Black, 64 GB)']")
    _Assured_checkbox=("xpath","//div[@class='XqNaEv eJE9fb']/../..//img[@class='SwtzWS']")
    _oopo_checkbox=("xpath","//div[text()='OPPO']/../..//div[@class='XqNaEv']")
    _all_oppo_mobiles=("xpath","//div[@class='KzDlHZ']")
    _add_cart_btn=("xpath","//button[@class='QqFHMw vslbG+ In9uk2']")
    _cart_btn=("xpath","//span[text()='Cart']")
    _place_order_btn=("xpath","//button[@class='QqFHMw zA2EfJ _7Pd1Fp']")

    def oppo(self):
        self.click_item(self._oppo)
    def assured_link(self):
        self.scroll_to_element(self._Assured_checkbox)
        #self.click_item(self._Assured_checkbox)
    def click_oppo_checkbox(self):
        self.click_item(self._oopo_checkbox)

    def get_all_oppo_mob(self):
        """Returns a dictionary of Oppo mobile names with their corresponding web elements"""
        elements = self.find_elements(self._all_oppo_mobiles)

        # Debugging: Print raw elements
        #print("Raw elements found:", elements)

        mobile_dict = {}

        for ele in elements:
            mobile_name = ele.text.strip()
            print(f"Mobile Found: {mobile_name}")  # Debugging
            if mobile_name:
                mobile_dict[mobile_name] = ele  # Store element with its name

        print("Extracted mobile dictionary:", mobile_dict)  # Debugging
        return mobile_dict
    def go_to_cart_button(self):
        self.swi
        self.scroll_to_element(self._add_cart_btn)
        self.click_item(self._add_cart_btn)
    def click_cart_btn(self):
        self.click_item(self._cart_btn)
    def click_place_order(self, locator):
        self.click_item(self._place_order_btn)




