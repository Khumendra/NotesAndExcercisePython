class Tomato():
    def type(self):
        print('Vegitable')

    def color(self):
        print('Red')


class Apple():
    def type(self):
        print('Fruit')

    def color(self):
        print('Red')



# executing somthing common 
def func(obj):
    obj.type()
    obj.color()


obj_tomato = Tomato()
obj_apple = Apple()

func(obj_tomato)
func(obj_apple)
