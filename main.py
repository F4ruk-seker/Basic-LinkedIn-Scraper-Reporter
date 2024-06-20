# user search with first name and last name >
from models.person_search_model import PersonSearchModel
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep


RESULT: list = []
DEFAULT_WAIT_TIME: int = 10

# temp
FIRST_NAME: str = 'Faruk'
LAST_NAME: str = 'şeker'

browser = Firefox()
browser.get('https://linkedin.com/')
sleep(DEFAULT_WAIT_TIME / 2)

person_nav_link = browser.find_element(By.XPATH, '/html/body/nav/ul/li[2]/a')
person_nav_link.click()

sleep(DEFAULT_WAIT_TIME / 2)
first_name = browser.find_element(By.XPATH, '//*[@id="people-search-panel"]/form/section[1]/input')
last_name = browser.find_element(By.XPATH, '//*[@id="people-search-panel"]/form/section[2]/input')

# load form
first_name.send_keys(FIRST_NAME)
sleep(DEFAULT_WAIT_TIME / 5)
last_name.send_keys(LAST_NAME)

search_button = browser.find_element(By.XPATH, '//*[@id="people-search-panel"]/form/button')
sleep(DEFAULT_WAIT_TIME / 10)
search_button.click()

sleep(DEFAULT_WAIT_TIME / 5)
person_list = browser.find_element(By.XPATH, '//*[@id="main-content"]/section/ul')


def get_object(frame, by, value, many: bool = False):
    try:
        return (frame.find_elements if many else frame.find_element)(by, value)
    except:
        # return [] if many else None
        return None


for person in person_list.find_elements(By.TAG_NAME, 'li'):

    person_search_data: PersonSearchModel = PersonSearchModel.load_default()
    if name := get_object(person, By.TAG_NAME, 'h3'):
        person_search_data.name = name.text
    if title := get_object(person, By.TAG_NAME, 'h4'):
        person_search_data.title = title.text
    if country := get_object(person, By.TAG_NAME, 'p'):
        person_search_data.country = country.text
    if details := get_object(person, By.TAG_NAME, 'span', many=True):
        person_search_data.details = [detail.text for detail in details]
    print(person_search_data)
    RESULT.append(person_search_data)

print("RESULT")
print(RESULT)
print("END")


