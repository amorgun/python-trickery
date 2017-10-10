class Foo(object):
    def who_am_i(self):
        print('I am Foo')

class Bar(object):
    def who_am_i(self):
        print('I am Bar')

obj = Foo()
obj.who_am_i()
obj.__class__ = Bar
obj.who_am_i()
