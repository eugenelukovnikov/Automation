#файл только для урока https://stepik.org/lesson/237240/step/10

import time
import pytest


from selenium import webdriver


def test_btn_add_to_cart_exist(browser):
    
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    #time.sleep(30)
    btn_add_cart = ("xpath", "//button[contains(@class,'btn-add-to-basket')]")
    btn_add_cart_check = browser.find_elements(*btn_add_cart)
    assert btn_add_cart_check, 'Кнопка "Добавить в корзину" отсутствует'

