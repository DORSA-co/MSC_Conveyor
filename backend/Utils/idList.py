class idList:

    def __init__(self) -> None:
        self.main_list = []
        self.ids_list = []
    
    def append(self, value, _id):
        self.main_list.append(value)
        self.ids_list.append(_id)
    
    def insert(self,index, value, _id):
        self.main_list.insert(index, value)
        self.ids_list.insert(index, _id)
    
    def remove_by_value(self, value):
        idx = self.main_list.index(value)
        self.main_list.pop(idx)
        self.ids_list.pop(idx)
    
    def remove_by_id(self, _id):
        idx = self.ids_list.index(_id)
        self.main_list.pop(idx)
        self.ids_list.pop(idx)
    
    def remove_by_index(self, idx):
        self.main_list.pop(idx)
        self.ids_list.pop(idx)

    def get_by_id(self, _id):
        idx = self.ids_list.index(_id)
        return idx, self.main_list[idx]

    def set_by_index(self, idx, value, _id):
        self.main_list[idx] = value
        self.ids_list[idx] = _id

    def count(self,):
        return len(self.main_list)
    
    def values(self,):
        return self.main_list
    
    def __getitem__(self, idx):
        return self.main_list[idx]
    
    def __len__(self):
        return len(self.main_list)