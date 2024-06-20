import json

from report import Report


class JsonReport(Report):
    output_settings: dict = {
        'defaultextension': '.json',
        'title': 'Save File',
        'initialfile': 'result.json',
        'filetypes': [("JSON files", "*.json"), ("All files", "*.*")]
    }

    def __init__(self, data):
        self.data = data
        self.load_report()

    def load_report(self):
        self.output = json.dumps(self.data)

    def save_report(self):
        json_file_path = self.asksaveasfilename()
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json_file.write(str(self.output))


if __name__ == '__main__':
    result_list = [{'name': 'Faruk Şeker', 'title': 'Full Stack Developer', 'country': 'Netherlands',
                    'details': ['Freelencer, +2 more', 'Anadolu Üniversitesi, +1 more'],
                    'photograph': 'https://media.licdn.com/dms/image/D4D03AQH1Z2dg7iz7MQ/profile-displayphoto-shrink_200_200/0/1709814396783?e=2147483647&v=beta&t=kwoc1SJRo3B6dfAWOxAWppBSYvnUM2mB8x8QsVmybAU'}]

    html_report = JsonReport(result_list)
    html_report.save_report()

