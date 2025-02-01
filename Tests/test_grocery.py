import pytest


@pytest.mark.regression
def test_grocery_page(pages):
 pages.homepage.grocery()  # Now, directly call grocery() without passing pages

 # Handle alert if needed (Make sure handle_alert is used properly)
 #pages.homepage.selenium_wrapper.handle_alert(action="send_keys", value="560078")




