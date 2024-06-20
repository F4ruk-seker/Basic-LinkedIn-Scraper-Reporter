if __name__ == '__main__':
    from base import Scraper
else:
    from .base import Scraper

from models.person_search_model import PersonSearchModel
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class PersonSearchScraper(Scraper):
    browser = Firefox()
    show_counter = True
    model = PersonSearchModel
    person_list = None

    def __init__(self, **kwargs):
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')
        super().__init__()

    def scrape(self):
        self.browser.get('https://linkedin.com/')
        self.sleep(5)

        person_nav_link = self.browser.find_element(By.XPATH, '/html/body/nav/ul/li[2]/a')
        person_nav_link.click()
        self.sleep(5)

        first_name = self.browser.find_element(By.XPATH, '//*[@id="people-search-panel"]/form/section[1]/input')
        last_name = self.browser.find_element(By.XPATH, '//*[@id="people-search-panel"]/form/section[2]/input')

        first_name.send_keys(self.first_name)
        self.sleep(2)
        last_name.send_keys(self.last_name)
        self.sleep(2)

        search_button = self.browser.find_element(By.XPATH, '//*[@id="people-search-panel"]/form/button')
        search_button.click()
        self.sleep(5)
        self.browser.execute_script('window.scrollTo(0, document.body.scrollHeight / 2)')
        self.sleep(2)
        self.browser.execute_script('window.scrollTo(0, document.body.scrollHeight / 2)')
        self.person_list = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/section/ul')

    def load_result(self):
        if self.person_list is not None:
            # //*[@id="main-content"]/section/ul/li[1] /a/div[1]/img
            for person in self.person_list.find_elements(By.TAG_NAME, 'li'):
                # actions = ActionChains(self.browser)
                # actions.move_to_element(person).perform()
                self.browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                                            person)
                self.sleep(.10)
                person_search_data = self.get_model().load_default()
                if name := self.get_object(person, By.TAG_NAME, 'h3'):
                    person_search_data.name = name.text
                if title := self.get_object(person, By.TAG_NAME, 'h4'):
                    person_search_data.title = title.text
                if country := self.get_object(person, By.TAG_NAME, 'p'):
                    person_search_data.country = country.text
                if details := self.get_objects(person, By.TAG_NAME, 'span'):
                    person_search_data.details = [detail.text for detail in details]
                if photograph := self.get_object(person, By.TAG_NAME, 'img'):
                    person_search_data.photograph = photograph.get_attribute('src')
                self.result.append(person_search_data)

    def get_result(self) -> list[PersonSearchModel]:
        self.load_result()
        return self.result

    def get_dict_result(self) -> list[dict]:
        return [result.__dict__ for result in self.get_result()]


if __name__ == '__main__':
    # temp
    FIRST_NAME: str = 'Faruk'
    LAST_NAME: str = 'şeker'

    scraper = PersonSearchScraper(first_name=FIRST_NAME, last_name=LAST_NAME)
    scraper.scrape()
    print(scraper.get_dict_result())
    del scraper
