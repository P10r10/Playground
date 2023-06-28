from employee import Employee
from pytest import fixture


@fixture
def employee_test():
    return Employee("a", "a", 5000)


def test_give_default_raise(employee_test):
    employee_test.give_raise()
    assert employee_test.annual_salary == 10000


def test_give_custom_raise(employee_test):
    employee_test.give_raise(10000)
    assert employee_test.annual_salary == 15000
