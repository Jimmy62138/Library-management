
def singleton(classe):
    _instance = {}

    def get_instance(*args, **kwargs):
        if classe not in _instance:
            _instance[classe] = classe(*args, **kwargs)
        return _instance[classe]
    return get_instance
   
   
@singleton 
class Bibliotheque():
    def __init__(self, value) -> None:
        self.value = value
        
        

        
        
if __name__ == "__main__":
    
    # test singleton
    test_singleton1 = Bibliotheque("Premier")
    test_singleton2 = Bibliotheque("Second")
    print(test_singleton1.value)
    print(test_singleton2.value)
    print(test_singleton1 is test_singleton2)
    
    