from TestStub import TestCaseTest
import TestSuiteTest
from test_loader import TestLoader
from my_test_runner import TestRunner
from test_loader_test import TestLoaderTest
from test_suite import TestSuite

loader = TestLoader()


test_case_suite = loader.make_suite(TestCaseTest)
test_suite_suite = loader.make_suite(TestSuiteTest)
test_loader_suite = loader.make_suite(TestLoaderTest)


suite = TestSuite()
suite.add_test(test_case_suite)
suite.add_test(test_suite_suite)
suite.add_test(test_loader_suite)


runner = TestRunner()
runner.run(suite)

result = runner.run(suite)
print(result.summary())