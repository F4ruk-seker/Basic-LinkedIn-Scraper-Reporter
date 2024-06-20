from abc import ABC
from time import sleep


class Scraper(ABC):
    browser = None
    show_counter = False
    model = None
    result = []

    def get_model(self):
        assert self.model is not None, (
            "'%s' should either include a `model` attribute, "
            "or override the `get_model()` method."
            % self.__class__.__name__
        )
        return self.model

    @staticmethod
    def get_objects(frame, by, value):
        try:
            return frame.find_elements(by, value)
        except:
            return None

    @staticmethod
    def get_object(frame, by, value):
        try:
            return frame.find_element(by, value)
        except:
            return None

    def get_result(self):
        raise NotImplementedError

    def scrape(self):
        raise NotImplementedError

    def sleep(self, time):
        if self.show_counter:
            for _ in range(time, 0, -1):
                print(f'\r{_}.second left', end='')
                sleep(1)
            print('\n')
        else:
            sleep(time)
