import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By




#иницилизирую драйвер браузера
driver = webdriver.Chrome()












try:
        # через get мы говорим браузеру что обращаемся к странице
    driver.get('https://erikdark.github.io/Qa_autotest_01/')
    time.sleep(2)
    #с помощью команды find_element(и класса By внутри ) мы ишем нужный элемент на странце сайта, в качестве аргумента мы передаем класс поиска By и значение которое ищем.
    input_one = driver.find_element(By.ID,'inputField')




    #с помощью send_keys(мы записываем данные в поле)
    input_one.send_keys('Erik')




    btn = driver.find_element(By.CSS_SELECTOR,".buttons .btn:nth-child(3)")
    #с помощью click() мы кликаем по кнопке
    btn.click()
    time.sleep(5)


finally:
    driver.quit()





driver.quit()


