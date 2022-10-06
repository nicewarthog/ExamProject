from time import sleep

from selenium import webdriver


class TestStartPage:

    def test_incorrect_login(self):
        driver = webdriver.Chrome(r"\Users\nicewarthog\PycharmProjects\ExamProject\chromedriver.exe")
        driver.get("https://vino.ua/")
        sleep(5)
        driver.close()
