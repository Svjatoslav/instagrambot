from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
username = 'angel21december'
password = '********'
# def login(username, password):
#     browser = webdriver.Chrome('C:/Users/user/PycharmProjects/instagrambot/chromedriver/chromedriver.exe')
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




print('Введите хэштег...')
ht = input()
time.sleep(2)
print('Введите колличество страниц для парсинга...')
count = input()



def hashtag_searh (username, password, hashtag):

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
    options.add_argument("--disable-blink-features=AutomationControlled")
    global posts_url
    browser = webdriver.Chrome('C:/Users/user/chrome/chromedriver.exe',
                               options=options)

    try:
        print('Входим на сайт....')
        browser.get('https://www.instagram.com/')
        time.sleep(random.randrange(3, 5))
        username_input = browser.find_element_by_name("username")
        username_input.clear()
        username_input.send_keys(username)
        time.sleep(5)

        password_input = browser.find_element_by_name("password")
        password_input.clear()
        password_input.send_keys(password)
        time.sleep(5)

        password_input.send_keys(Keys.ENTER)
        time.sleep(6)
        print('Вошли....')
        time.sleep(5)


        try:
            print('Переходим на страничку с хэштегами....')
            browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
            time.sleep(5)
            posts_url = []
            page = 1
            for page in range(1,int(count)):
                print('Собираем ссылки - ', page)
                time.sleep(random.randrange(3,5))

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


            for i in range(len(posts_url)):

                browser.get(posts_url[i])

                if browser.find_element_by_xpath("//button[@class='wpO6b  ']/div/span/*[name()='svg'][@aria-label]").get_attribute('aria-label') == 'Нравится':
                    like_button = browser.find_element_by_xpath('/html/body/div[1]/div/div/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
                    print(f'Поставили лайкос на пост по {i + 1}-ой ссылке')

                    time.sleep(random.randrange(110,130))
            browser.close()
            browser.quit()
        except FileExistsError as ex:
                print(ex)
    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()
hashtag_searh(username, password, ht)
