class A(object):
    def __init__(self, data = None):
        self.data = data

    def method_a(self, foo):
        print(str(self.data) + ' ' + foo)

if __name__ == '__main__':
    a = A(100)
    a.method_a('sailor!')
