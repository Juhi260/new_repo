from Library.genericUtilities import SeleniumWrapper


class HomePage(SeleniumWrapper):
    _grocery_img=("xpath","//img[@alt='Kilos']")
    _mobile_img=("xpath","//img[@alt='Mobiles']")
    _fashion_img = ("xpath", "//img[@alt='Fashion']")
    _home_furniture_img = ("xpath", "//img[@alt='Home & Furniture']")
    _electronics_img = ("xpath", "//img[@alt='Electronics']")
    _appliances_img=("xpath", "//img[@alt='Appliances']")
    _flight_book_img = ("xpath", "//img[@alt='Flight Bookings']")
    _beauty_toys_more_img = ("xpath", "//img[@alt='Beauty, Toys & More']")
    _two_wheeler_img = ("xpath", "//img[@alt='Two Wheelers']")
    _search_field=("xpath","//input[@title='Search for Products, Brands and More']")
    _search_btn=("xpath","//button[@aria-label='Search for Products, Brands and More']")
    _login_btn=("xpath","//div[@class='H6-NpN _3N4_BX']")

    def __init__(self, driver):
        super().__init__(driver)

    def grocery(self):
        self.click_item(self._grocery_img)

    def mobile(self):
        self.click_item(self._mobile_img)

    def fashion(self):
        self.click_item(self._fashion_img)

    def furniture(self):
        self.click_item(self._home_furniture_img)

    def electronics(self):
        self.click_item(self._electronics_img)

    def appliance(self):
        self.click_item(self._appliances_img)

    def flight(self):
        self.click_item(self._flight_book_img)

    def beauty(self):
        self.click_item(self._beauty_toys_more_img)

    def two_wheeler(self):
        self.click_item(self._two_wheeler_img)
    def search(self):
        self.send_item(self._search_field,"Mobile")
        self.click_item(self._search_btn)
    def login(self):
        self.click_item(self._login_btn)



