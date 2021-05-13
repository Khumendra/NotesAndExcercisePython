# private:  _var
# protected: __var

class ClassName:
    x = 12

    # private
    _y = 10

    # protected
    __z  = 20

my_class = ClassName()

print("x:",my_class.x)
print('Private y:',my_class._y)
print("Protected z:",my_class._ClassName__z)