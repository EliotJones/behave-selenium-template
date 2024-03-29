from .browsers import Browsers 
from helpers import configuration
import os
from selenium import webdriver

def capture_failure(context, scenario):
    originalpath = os.getcwd()
    path = os.path.join(configuration.projectRoot, "failures")
    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)
    context.browser.maximize_window()
    context.browser.save_screenshot(scenario.name + ".png")
    os.chdir(originalpath)