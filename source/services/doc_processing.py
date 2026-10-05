import os
from abc import ABC, abstractmethod


class Document(ABC):

    _protected = 1

    def __init__(self, path):
        self._path = path

    @abstractmethod
    def intake_document(self):
        pass

    # @abstractmethod
    # def find_vat_return(self):
    #     pass
    #
    # @abstractmethod
    # def find_total_income(self):
    #     pass
    #
    # @abstractmethod
    # def export_document(self):
    #     pass


class PDF_reader(Document):
    def __init__(self, path, name):
        super().__init__(path)
        self.name = name

    def intake_document(self):
        path = self._protected
        print(path)


if __name__ == "__main__":
    pdf = PDF_reader("/docs/M99C0E1-000001", "doc1")
    print(pdf.intake_document())
