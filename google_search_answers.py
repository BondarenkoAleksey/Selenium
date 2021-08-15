from selenium import webdriver

browser = webdriver.Chrome()
list1 = []  # создание пустого списка
link1 = "https://www.google.com/search?q=купить+кофемашину+bork+c804"  # страница поиска
browser.get(link1)  # переход на страницу поиска
links = browser.find_elements_by_css_selector(
    " div.yuRUbf > a")  # поиск элементов по общему для поисковых ответов CSS-селектору
for link in links:  # запускаем цикл получения ссылок с сохранением в список
    list1.append(link.get_attribute("href"))
print(list1)
browser.quit() # закрытие браузера