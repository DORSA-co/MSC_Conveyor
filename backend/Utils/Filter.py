import numbers

class applyFilter:

    def __init__(self, filter_refrence:dict = dict()) -> None:
        self.filter_refrence = filter_refrence

    def clear_filters(self,):
        self.filter_refrence = dict()
    
    def set_filters_refrence(self, filter_refrence):
        self.filter_refrence = filter_refrence

    def check_filter(self, data:dict):
        
        #check if no filter exist
        if len(self.filter_refrence) == 0:
            return True
        
        for name, value in data.items():
            _filter_value = self.filter_refrence.get(name)
            if _filter_value is None:
                continue

            #-------------------------------------------                    
            if isinstance(_filter_value, tuple):
                if isinstance(value, numbers.Number):
                    if value < _filter_value[0] or value  > _filter_value[1]:
                        return False
                
                elif isinstance(value, tuple):
                    if value[0] > _filter_value[1] or value[1] < _filter_value[0]:
                        return False
            
            #-------------------------------------------
            elif isinstance(_filter_value, bool):
                if value!=_filter_value:
                    return False
            
            #-------------------------------------------
            elif isinstance(_filter_value, set):
                if value not in _filter_value:
                    return False
        return True                
