#가시성(visibility) : 정보은닉
#비공개 필드, 비공개 메서드
#비공개 필드는 직접접근가능한 메서드를 구현하여 사용하거나

# 예. Product 클래스와 Inventory 클래스


class Product(object):
    pass
class Inventory(object):
    def __init__(self):
        self.__items = []

    def addNewitem(self, product):
        if type(product) == Product:
            self.__items.append(product)
            print('new item added')
        else:
            print('error')

    def getNumberofItems(self):
        return len(self.__items)

    def getItems(self):
        print(self.__itmes)

    #데코레이터 @property를 사용하여 비공개 필드를 직접 접근하여 사용
    @property
    def items(self):
        return self.__items

myInvent = Inventory()
myInvent.addNewitem(Product())
myInvent.addNewitem(Product())
myInvent.addNewitem(Product())

myInvent.getItems()
print(myInvert.items)