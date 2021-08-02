from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

try:
    link = "https://www.dns-shop.ru/"
    browser = webdriver.Chrome()
    browser.get(link)
    random = random.randint(1, 3)
    phone_number = "9012345678"

    #переход по категориям товаров
    appliances = browser.find_element_by_css_selector("div:nth-child(1) > div.menu-desktop__root-info > a")
    appliances.click()

    time.sleep(random)

    kitchen_appliances = browser.find_element_by_xpath("//div[1]/a[1]/div[1]/span")
    kitchen_appliances.click()

    time.sleep(random)

    preparation_of_drinks = browser.find_element(By.CSS_SELECTOR, "a:nth-child(3) > div.subcategory__content > div > picture > img")
    preparation_of_drinks.click()

    time.sleep(random)

    distillers = browser.find_element(By.XPATH, "//a[12]/div[1]/div/picture/img")
    distillers.click()

    time.sleep(random)

    #кнопка покупки
    buy_button = browser.find_element_by_css_selector("body > div.container.category-child > div > div.products-page__content > div.products-page__list > div.products-list > div > div.catalog-products.view-simple > div:nth-child(2) > div.product-buy.product-buy_one-line.catalog-product__buy > button.button-ui.buy-btn.button-ui_brand")
    buy_button.click()

    time.sleep(random)

    shopping_cart = browser.find_element(By.XPATH, "//div[2]/a[3]/span[3]/span[1]")
    shopping_cart.click()

    time.sleep(random)

    #переход в корзину
    place_an_order = browser.find_element_by_xpath('//*[@id="total-amount"]/div/div[2]/button')
    place_an_order.click()

    time.sleep(random)

    #ввод номера телефона
    phone = browser.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/input")
    phone.send_keys(phone_number)

    time.sleep(random)

    #оплата при получении
    upon_receipt = browser.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]")
    upon_receipt.click()

    time.sleep(random)

    #отказ от регистрации в программе ProZaPas
    uncheck = browser.find_element_by_xpath('//div[1]/label[1]/span[1]')
    uncheck.click()

    time.sleep(random + 1)

    #подтверждение заказа
    confirm_the_order = browser.find_element_by_css_selector("div.checkout-container__apply-wrapper > div > div")
    confirm_the_order.click()

    time.sleep(random - 1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()