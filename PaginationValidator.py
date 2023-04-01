import math
class PaginationHelper:

    
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page


    def item_count(self):
        if len(self.collection) != 0:
            return len(self.collection)
        else:
            return -1
      
    def page_count(self):
        self.amount_pages =  math.ceil(len(self.collection)/self.items_per_page)
        return self.amount_pages
       
    def page_item_count(self, page_index):
        counter = 0
        counter += (page_index + 1)*self.items_per_page
        if counter <= len(self.collection) and page_index >= 0:
            return self.items_per_page
        if counter - self.items_per_page == len(self.collection) - len(self.collection) % self.items_per_page and page_index >= 0:
            return len(self.collection) % self.items_per_page
        else:
            return -1
    
    def page_index(self, item_index):
        if item_index <= 0 or item_index >= len(self.collection):
            return -1
        
        else:
            return int(item_index/self.items_per_page)

        
run = PaginationHelper(["a"],4)
print(run.page_index(0))
        