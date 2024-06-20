if __name__ == '__main__':
    from base import Scraper
else:
    from .base import Scraper

from models.person_search_model import PersonSearchModel
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By


# temp
FIRST_NAME: str = 'Faruk'
LAST_NAME: str = 'şeker'


class PersonSearchScraper(Scraper):
    browser = Firefox()
    show_counter = True
    model = PersonSearchModel
    person_list = None

    def scrape(self):
        self.browser.get('https://linkedin.com/')
        self.sleep(5)

        person_nav_link = self.browser.find_element(By.XPATH, '/html/body/nav/ul/li[2]/a')
        person_nav_link.click()
        self.sleep(5)

        first_name = self.browser.find_element(By.XPATH, '//*[@id="people-search-panel"]/form/section[1]/input')
        last_name = self.browser.find_element(By.XPATH, '//*[@id="people-search-panel"]/form/section[2]/input')

        first_name.send_keys(FIRST_NAME)
        self.sleep(2)
        last_name.send_keys(LAST_NAME)
        self.sleep(2)

        search_button = self.browser.find_element(By.XPATH, '//*[@id="people-search-panel"]/form/button')
        search_button.click()
        self.sleep(5)

        self.person_list = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/section/ul')

    def load_result(self):
        if self.person_list is not None:
            for person in self.person_list.find_elements(By.TAG_NAME, 'li'):
                person_search_data = self.get_model().load_default()
                if name := self.get_object(person, By.TAG_NAME, 'h3'):
                    person_search_data.name = name.text
                if title := self.get_object(person, By.TAG_NAME, 'h4'):
                    person_search_data.title = title.text
                if country := self.get_object(person, By.TAG_NAME, 'p'):
                    person_search_data.country = country.text
                if details := self.get_objects(person, By.TAG_NAME, 'span'):
                    person_search_data.details = [detail.text for detail in details]
                self.result.append(person_search_data)

    def get_result(self) -> list[PersonSearchModel]:
        self.load_result()
        return self.result

    def get_dict_result(self) -> list[dict]:
        return [result.__dict__ for result in self.get_result()]


if __name__ == '__main__':
    scraper = PersonSearchScraper()
    scraper.scrape()
    print(scraper.get_dict_result())

