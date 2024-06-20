from jinja2 import Template, Environment
from config import TEMPLATE_DIR, BASE_DIR
from report import Report


class HtmlReport(Report):
    output_settings: dict = {
        'defaultextension': '.html',
        'title': 'Save File',
        'initialfile': 'result.html',
        'filetypes': [("HTML files", "*.html"), ("All files", "*.*")]
    }

    def __init__(self, data):
        self.data = data
        self.load_report()

    def load_report(self):
        with open(TEMPLATE_DIR / 'person_search_list.html', encoding='utf-8') as template_file:
            template = Template(template_file.read())
            self.output = template.render({'persons': self.data})

    def save_report(self):
        output_path = self.asksaveasfilename()
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(self.output)


if __name__ == '__main__':
    result_list = [{'name': 'Faruk Şeker', 'title': 'Full Stack Developer', 'country': 'Netherlands',
                    'details': ['Freelencer, +2 more', 'Anadolu Üniversitesi, +1 more'],
                    'photograph': 'https://media.licdn.com/dms/image/D4D03AQH1Z2dg7iz7MQ/profile-displayphoto-shrink_200_200/0/1709814396783?e=2147483647&v=beta&t=kwoc1SJRo3B6dfAWOxAWppBSYvnUM2mB8x8QsVmybAU'}]

    html_report = HtmlReport(result_list)
    html_report.save_report()
