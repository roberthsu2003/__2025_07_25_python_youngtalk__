class Person:
    def __init__(self,name):
        #self.name = name #建立attribute
        self.__name__ = name #private __name__,透過實體,不可以讀,也不可以寫入
    
    @property
    def name(self)->str:
        return self.__name__
    
    def __repr__(self):
        return f"我是{self.__name__}"
    
def main():
    p1 = Person("robert")
    print(p1)

    p2 = Person("jenny")
    print(p2)

if __name__ == "__main__":
    main()