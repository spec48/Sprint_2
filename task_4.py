class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email is None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment

    def salary(self):
        weekly_salary = self.hours * self.hourly_payment
        return weekly_salary


worker = EmployeeSalary.get_hours("Evgeniy", None, 2, None)
worker = EmployeeSalary.get_email(worker.name, worker.hours, worker.rest_days, worker.email)
EmployeeSalary.set_hourly_payment(500)
print(worker.email)
print(worker.salary())