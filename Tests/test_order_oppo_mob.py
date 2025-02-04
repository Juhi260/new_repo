from time import sleep
from Library.customLogger import LogGen
import pytest

logger=LogGen.loggen()
@pytest.mark.regression
def test_scroll_to_assured(pages):

    logger.info("testing test_scroll_to_assured")
    pages.homepage.mobile()
    sleep(5)
    pages.mobilepage.assured_link()
    sleep(3)
    pages.mobilepage.click_oppo_checkbox()
    sleep(3)
    Mobile_names=pages.mobilepage.get_all_oppo_mob()
    target_mobile="OPPO K12x 5G with 45W SUPERVOOC Charger In-The-Box (Midnight Violet, 256 GB)"
    if target_mobile in Mobile_names:
        Mobile_names[target_mobile].click()
        logger.info("clicked")
    else:
        logger.info("mobile not found")
    # pages.mobilepage.go_to_cart_button()
    # print("added to cart")
    # #pages.mobilepage.click_cart_btn()
    # #print("went to cart")
    # pages.mobilepage.click_place_order()
    # print("order placed")





