class TestCase:

    def __init__(self, test_method_name):
        self.test_method_name = test_method_name

    def run(self):
        self.set_up()   
        test_method = getattr(self, self.test_method_name)
        test_method()   
        self.tear_down() 

    def set_up(self):
        pass

    def tear_down(self):
        pass
    
    
    
class MyTest(TestCase):

    def set_up(self):
        print('set_up')

    def tear_down(self):
        print('tear_down')

    def test_a(self):
        print('test_a')

    def test_b(self):
        print('test_b')

    def test_c(self):
        print('test_c')


test = MyTest('test_a')
test.run()

test = MyTest('test_b')
test.run()

test = MyTest('test_c')
test.run()

