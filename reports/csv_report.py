from report import Report
import csv


class CsvReport(Report):
    fieldnames = ['name', 'title', 'country', 'details', 'photograph']
    output_settings: dict = {
        'defaultextension': '.csv',
        'title': 'Save File',
        'initialfile': 'result.csv',
        'filetypes': [("CSV files", "*.csv"), ("All files", "*.*")]
    }

    def __init__(self, data):
        self.data = data

    def load_report(self, csv_file_path):
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            for item in self.data:
                item['details'] = '; '.join(item['details']) if item['details'] else ''
                writer.writerow(item)

    def save_report(self):
        if csv_file_path := self.asksaveasfilename():
            self.load_report(csv_file_path)


if __name__ == '__main__':
    result_list = [{'name': 'Faruk Şeker', 'title': 'Full Stack Developer', 'country': 'Netherlands',
                    'details': ['Freelencer, +2 more', 'Anadolu Üniversitesi, +1 more'],
                    'photograph': 'https://media.licdn.com/dms/image/D4D03AQH1Z2dg7iz7MQ/profile-displayphoto-shrink_200_200/0/1709814396783?e=2147483647&v=beta&t=kwoc1SJRo3B6dfAWOxAWppBSYvnUM2mB8x8QsVmybAU'}]

    html_report = CsvReport(result_list)
    html_report.save_report()
