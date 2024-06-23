#가시성(visibility) : 정보은닉
#비공개 필드, 비공개 메서드
#비공개 필드는 직접접근가능한 메서드를 구현하여 사용하거나
# 데코레이터(@property) 를 이용하여 직접사용


# 예. Product 클래스와 Inventory 클래스

class Product(object):
    pass

class Inventory(object):
    def __init__(self):
        self.__items = []

    def addNewItem(self, product):
        if type(product) == Product:
            self.__items.append(product)
            print('new item added')
        else:
            print('error')

    def getNumberOfItems(self):
        return len(self.__items)

    def getItems(self):
        print(self.__items)

    #데코레이터 @property를 사용하여 비공개 필드를 직접 접근하여 사용
        @property
        def items(self):
            return self.__items

myInvent = Inventory()
myInvent.addNewItem(Product()) #결과: new item added
myInvent.addNewItem(Product()) #결과: new item added
myInvent.addNewItem(Product()) #결과: new item added
myInvent.addNewItem(Product()) #결과: new item added
myInvent.getItems()
#결과:
#[<__main__.Product object at 0x100f73e50>, <__main__.Product object at 0x100f73ca0>, <__main__.Product object at 0x100f73c40>, <__main__.Product object at 0x100f73c10>]

# print(myInvent.__items)
#print(myInvent.items)
