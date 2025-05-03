from test_suite import TestSuite
from test_case import TestCase

class TestLoader:

    TEST_METHOD_PREFIX = 'test'

    def get_test_case_names(self, test_case_class):
        methods = dir(test_case_class)
        return list(filter(lambda method: method.startswith(self.TEST_METHOD_PREFIX), methods))

    def make_suite(self, test_case_class):
        suite = TestSuite()
        for test_method_name in self.get_test_case_names(test_case_class):
            suite.add_test(test_case_class(test_method_name))
        return suite
