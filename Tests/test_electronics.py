import pytest


@pytest.mark.sanity
def test_electronics(pages):
 pages.homepage.electronics()