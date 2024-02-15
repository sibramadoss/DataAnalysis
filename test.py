class A(object):
    def __init__(self, data = 0):
        self.data = data
        #data is set to 0 if the value is not inputted by user

    def method_a(self, foo = 'twitter'):
        print(str(self.data) + ' ' + foo)

class B(object):
    x = 'hello'

    def __init__(self, data = 0, x = None, y = None):
        self.x = None
        self.y = None
        self.data = data
        #self.data = 7 locks in value and takes precedent over input arguments
        #once you set the x or y values inside the class it takes the most recent definition
        #self.x and self.y are placeholders for time being that set in later functions
        #or set one of input variables in function to self.x or self.y
        ##if you dont specify what x and y should be in the input arguments then you need to show it in the def __init__ input parameters

    def method_a(self, foo):
        self.x = foo
        self.y = 'seven'
        print (self.y + ' ' + self.x + ' ' + str(self.data))

    def summing(self, data2):
        print('summing: ' + str(self.data + data2))

    def subtracting(self, inp):
        print(self.x + ' '+ str(inp))
        #self.x carries over from function to function with the same value if established in a prior function

    def randsx(self, data):
        print(B.x + ' ' + str(data))


if __name__ == '__main__':
    a = A(100)
    a.method_a('sailor!')
    # try a = A()
    # if we dont initialize A with anything, the initial value is set to the default value in the arguments


    print(B.x)
    b = B(10)
    b.method_a('buddy!')
    b.summing(60)
    b.subtracting(12)
    b.randsx(12)
    print(b.x)
    print(b.y)
    #print(B.x*A(100).data) #throws back hello 100 times


# https://www.tutorialspoint.com/What-is-difference-between-self-and-init-methods-in-python-Class
# https://stackoverflow.com/questions/625083/what-do-init-and-self-do-in-python




