class Employee:
    def __init__(self, first_name: str, last_name: str, annual_salary: int):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__annual_salary = annual_salary

    @property
    def annual_salary(self):
        return self.__annual_salary

    def give_raise(self, amount: int = 5000):
        self.__annual_salary += amount
