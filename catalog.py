
class Catalog():
    def __init__(self, cat_title ):
        self.cat_title = cat_title
        self.cat_items = []

    def add_item(self, item):
        if self.cat_items and not any(cat_item["title"] == item.title and cat_item["author"] == item.author 
                                  for cat_item in self.cat_items):
            dict_item = {
                "title": item.title,
                "author": item.author,
                "year": item.year,
                "id": item.id,
                "status": item.status
            }
            self.items.append(dict_item)


    def remove_item(self, item):
        if any(cat_item["title"] == item.title and cat_item["author"] == item.author for cat_item in self.cat_items):
            self.cat_items.remove(item)         #needs to be fixed
    
    
    def search_by_title(self, title):
        if any(cat_item["title"] == title for cat_item in self.cat_items):
            return [cat_item for cat_item in self.cat_items if cat_item["title"] == title]

    def search_by_author(self, author):
        if any(cat_item["author"] == author for cat_item in self.cat_items):
            return [cat_item for cat_item in self.cat_items if cat_item["author"] == author]


