
class Catalog():
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def search_by_title(self, title):
        pass

    def search_by_author(self, author):
        pass

    def search_by_year(self, year):
        pass

    def search_by_type(self, item_type):
        pass
