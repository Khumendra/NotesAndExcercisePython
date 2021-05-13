class A:
    def sayhi(self):
        print("I'm in A")


class B(A):
    # def sayhi(self):
    #     print("I'm in B")
    pass

b_obj = B()
b_obj.sayhi()