from selenium import webdriver
import pytest

@pytest.fixture()
def driver():
    browser = webdriver.Chrome()
    return browser