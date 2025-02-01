import pytest


@pytest.mark.regression
def test_fashion_link(pages):
 pages.homepage.fashion()