from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

username = 'angel21december'
password = 'lena1110'


# def login(username, password):
#     browser = webdriver.Chrome()
#
#     try:
#         browser.get('https://www.instagram.com/')
#         time.sleep(random.randrange(3, 5))
#
#         username_input = browser.find_element_by_name('username')
#         username_input.clear()
#         username_input.send_keys(username)
#
#         time.sleep(2)
#
#         password_input = browser.find_element_by_name('password')
#         password_input.clear()
#         password_input.send_keys(password)
#
#         password_input.send_keys(Keys.ENTER)
#
#         time.sleep(10)
#
#         browser.close()
#         browser.quit()
#     except Exception as ex:
#         print(ex)
#         browser.close()
#         browser.quit()
#
# login(username, password)


def hashtag_searh (username, password, hashtag, count):

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
    options.add_argument("--disable-blink-features=AutomationControlled")
    global posts_url
    browser = webdriver.Chrome(options=options)

    try:
        print('Входим на сайт....')
        browser.get('https://instagram.com/accounts/login')
        time.sleep(5)
        username_input = browser.find_element_by_name("username")
        username_input.clear()
        username_input.send_keys(username)
        time.sleep(1)

        password_input = browser.find_element_by_name("password")
        password_input.clear()
        password_input.send_keys(password)
        time.sleep(1)

        password_input.send_keys(Keys.ENTER)
        time.sleep(5)
        # print(browser.current_url)
        # print(browser.page_source)
        print('Вошли....')

        try:
            print('Переходим на страничку с хэштегами....')
            browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
            time.sleep(5)

            posts_url = []
            page = 1
            for page in range(1, count):
                print('Собираем ссылки - ', page)
                time.sleep(3)

                hrefs = browser.find_elements_by_tag_name('a')


                for item in hrefs:
                    href = item.get_attribute('href')
                    if '/p/' in href:
                        posts_url.append(href)
                page += 1
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                print(f'Cобрано {len(posts_url)} ссылок ')
            set_posts_urls = set(posts_url)
            posts_url = list(set_posts_urls)


            for url in posts_url:
                print(url)
                browser.get(url)

                if browser.find_element_by_xpath("//button[@class='wpO6b  ']/div/span/*[name()='svg'][@aria-label]").get_attribute('aria-label') == 'Like':
                    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button"))).click()
                    print(f'Поставили лайкос на пост по ссылке {url}')

                    time.sleep(random.randrange(110,130))
            browser.close()
            browser.quit()
        except FileExistsError as ex:
            print('внутренний вылет')
            print(ex)
    except Exception as ex:
        print('внешний вылет')
        print(ex)
        browser.close()
        browser.quit()

if __name__ == '__main__':
    names = ['Виталиночку', 'Полиночку (1)','Полиночку (2)','Полиночку (3)', 'Диночку', 'Анечку', 'Алиночку','Софочку']
    print('******************************')
    print(f'Вот бы {random.choice(names)} трахнуть...')
    print('******************************')
    print('Введите хэштег...')
    ht = input()
    print('Введите колличество страниц для парсинга...')
    count = int(input())
    hashtag_searh(username, password, ht, count)
