from abc import ABC
from tkinter import filedialog


class Report(ABC):
    output = None
    output_settings: dict = {
                                'defaultextension': '.pdf',
                                'title': 'Save File',
                                'initialfile': 'result.pdf',
                                'filetypes': [("PDF files", "*.pdf"), ("All files", "*.*")]
                            }

    def load_report(self):
        raise NotImplementedError

    def save_report(self):
        raise NotImplementedError

    def asksaveasfilename(self):
        return filedialog.asksaveasfilename(**self.output_settings)

        # if file_path:  # asksaveasfilename "İptal" ile kapatıldığında boş bir string döner
        #     with open(file_path, 'w') as file:  # Dosyayı aç
        #         text_to_save = "fdsgdsahfd.test"  # Kaydedilecek metin
        #         file.write(text_to_save)  # Metni dosyaya yaz
        #
