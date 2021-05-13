# Multi-Level Inheritance


class A(object):
    _message = "message from A"


class B(A):
    def message(self):
        message = "message from B."
        return message


class C(B):
    def c_message(self):
        msg = "Child Message"
        return msg


cObj = C()

print(
    cObj._message,
    cObj.message(),
    cObj.c_message(),
    sep="\n"
)
