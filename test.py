class A(object):
    def __init__(self, data = None):
        self.data = data

    def method_a(self, foo):
        print(str(self.data) + ' ' + foo)

class B(object):
    x = 'hello'

    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def method_a(self, foo):
        print (self.y + ' ' + self.x + ' ' + foo)


if __name__ == '__main__':
    a = A(100)
    a.method_a('sailor!')

    print(B.x)
    b = B('bar', 'hello')
    print(b.x)
    print(b.y)
    b.method_a('buddy!')


# https://www.tutorialspoint.com/What-is-difference-between-self-and-init-methods-in-python-Class
# https://stackoverflow.com/questions/625083/what-do-init-and-self-do-in-python




