class A(object):
    def __init__(self, data = None, x = None):
        self.data = data
        self.x = 7

    def method_a(self, foo):
        print(str(self.data) + ' ' + foo)

class B(object):
    x = 'hello'

    def __init__(self, data):
        self.x = None
        self.y = None
        self.data = data
        #self.data = 7 locks in value and takes precedent over input arguments
        #once you set the x or y values inside the class it takes the most recent definition
        #self.x and self.y are placeholders for time being that set in later functions
        #or set one of input variables in function to self.x or self.y

    def method_a(self, foo):
        self.x = foo
        self.y = 'seven'
        print (self.y + ' ' + self.x + ' ' + ' ' + str(self.data))

    def summing(self, data2):
        print(self.data + data2)

    def subtracting(self, inp):
        print(self.x + ' '+ str(inp))

    def randsx(self, data):
        print(B.x + str(data))


if __name__ == '__main__':
    a = A(100)
    a.method_a('sailor!')


    print(B.x)
    b = B(57)
    b.method_a('buddy!')
    b.summing(60)
    b.subtracting(12)
    b.randsx(12)
    print(b.x)
    print(b.y)
    #print(B.x*A(100).data) #throws back hello 100 times


# https://www.tutorialspoint.com/What-is-difference-between-self-and-init-methods-in-python-Class
# https://stackoverflow.com/questions/625083/what-do-init-and-self-do-in-python




