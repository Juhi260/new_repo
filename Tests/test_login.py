import pytest


@pytest.mark.sanity
def test_login_btn(pages):
 pages.homepage.login()