class A(object):
    def __init__(self):
        print "A!"

class B(A):
    def __init__(self):
        super(B, self).__init__()
        print "B!"

class C(A):
    def __init__(self):
        super(C, self).__init__()
        print "C!"

class D(B, C):
    def __init__(self):
        super(D, self).__init__()
        print "D!"

print D.mro()
D()
print D
ob=D()
print ob.__dict__.keys()
print ob.__dict__.values()
print D.__dict__