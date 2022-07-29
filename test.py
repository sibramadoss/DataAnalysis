class A(object):
    def __init__(self, data = None):
        self.data = data

    def method_a(self, foo):
        print(str(self.data) + ' ' + foo)

class B(object):
    x = 'hello'

    def __init__(self, x=None, y=None, data=None):
        self.x = x
        self.y = y
        self.data = data
        #self.data = 7 locks in value and takes precedent over input arguments

    def method_a(self, foo):
        print (self.y + ' ' + self.x + ' ' + foo + ' ' + str(self.data))

    def summing(self, data2):
        print(self.data + data2)

    def subtracting(self, inp):
        print(self.x + ' '+ str(inp))


if __name__ == '__main__':
    #a = A(100)
    #a.method_a('sailor!')


    print(B.x)
    b = B('bar', 'hello', 57)
    b.method_a('buddy!')
    b.summing(60)
    b.subtracting(12)
    #print(B.x*A(100).data) #throws back hello 100 times


# https://www.tutorialspoint.com/What-is-difference-between-self-and-init-methods-in-python-Class
# https://stackoverflow.com/questions/625083/what-do-init-and-self-do-in-python




