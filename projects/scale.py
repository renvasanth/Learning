
class Vegetable(object):

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight    
    
class Scale(object):
    
    def __init__(self):
        self.items = []
        self.weight = 0
                            
    def add_item(self, item):
        self.items.append(item)     
        self.weight = self.weight + item.weight
        return self.weight
        
    def remove_item(self, name):
        for veg in self.items:
            if name == veg.name:
                self.items.remove(veg)
                self.weight = self.weight - veg.weight
        return self.weight
            
    def list_items(self):
        li = []
        for vg in self.items:
            li.append(vg.name)
        return li
        
if __name__ == "__main__":
    print Scale().add_item('tomoto', 1.4)
    print Scale().add_item('mango', 2.3)
