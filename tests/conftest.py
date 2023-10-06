import pytest
import selenium.webdriver
import json


@pytest.fixture


def browser():
    
    #initialize chromedriver(wd)
    b=selenium.webdriver.Chrome()
    
    #wait 10 sec for element to apper
    b.implicitly_wait(10)

    #return wd for the setup
    yield b

    #quit the wd for clean up
    b.quit()