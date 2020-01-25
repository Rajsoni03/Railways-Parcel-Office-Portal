# # from selenium import webdriver
# # import pyautogui as gui
# #
# # driver = webdriver.Chrome(executable_path=r'C:/Program Files/chromedriver.exe')
# # driver.get('http://127.0.0.1:8080/dashboard')
# # con = gui.confirm('Start')
# #
# # if con == 'OK':
# #     user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name)).click()
# #     msg_box = driver.find_element_by_class_name('_3u328')
# #     for i in range(count):
# #         msg_box.send_keys(msg)
# #         print(i)
# #         btn = driver.find_element_by_class_name('_3M-N-').click()
# #
# # driver = webdriver.Chrome(executable_path=r'C:/Program Files/chromedriver.exe')
# #
# # response = webdriver.request('POST',
# #                              'http://127.0.0.1:8080/myAdmin/update',
# #                              data={"train_ID": "2",
# #                                    'lat': 72.16378,
# #                                    'long': 29.72381,
# #                                    'seal_status': True,
# #                                    'parcel_status': True
# #                                    }
# #                              )
# # print(response)
#
# # import requests
# #
# URL = "http://127.0.0.1:8080/dashboard"
# #
# # PARAMS = {"train_ID": "2",
# #            'lat': 72.16378,
# #            'long': 29.72381,
# #            'seal_status': True,
# #            'parcel_status': True,
# #             csrfmiddlewaretoken=csrftoken
# #            }
# # requests.post(URL, PARAMS)
# import sys
# import requests
#
# client = requests.session()
#
# # Retrieve the CSRF token first
# client.get(URL)  # sets cookie
# if 'csrftoken' in client.cookies:
#     # Django 1.6 and up
#     csrftoken = client.cookies['csrftoken']
# else:
#     # older versions
#     csrftoken = client.cookies['csrf']
#
# PARAMS = {"train_ID": "2",
#            'lat': 72.16378,
#            'long': 29.72381,
#            'seal_status': True,
#            'parcel_status': True,
#             'csrfmiddlewaretoken': csrftoken,
#            }
# login_data = dict(username='Raj@gmail.com', password='1234', csrfmiddlewaretoken=csrftoken)
# r = client.post(URL, data=login_data, headers=dict(Referer="http://127.0.0.1:8080/login"))
# r = client.post(URL, data=PARAMS, headers=dict(Referer="http://127.0.0.1:8080/dashboard/update"))
#
#
# import sys
#
# import django
# from django.middleware.csrf import CsrfViewMiddleware, get_token
# from django.test import Client
#
# django.setup()
# csrf_client = Client(enforce_csrf_checks=True)
#
# URL = 'http://127.0.0.1/login'
# EMAIL= 'Raj@gmail.com'
# PASSWORD= '1234'
#
# # Retrieve the CSRF token first
# csrf_client.get(URL)  # sets cookie
# csrftoken = csrf_client.cookies['csrftoken']
#
# login_data = dict(username=EMAIL, password=PASSWORD, csrfmiddlewaretoken=csrftoken.value, next='/')
# r = csrf_client.post(URL, data=login_data, headers=dict(Referer=URL))



number = int(input("enter a number: "))
sqrt = number ** 0.25
print("square root:", sqrt)