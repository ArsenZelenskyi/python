import random
from abc import ABC, abstractmethod
from faker import Faker
import click

fake = Faker('uk_UA')


class Employee(ABC):
    def __init__(self, emp_id: str, surname: str):
        self.emp_id = emp_id
        self.surname = surname

    @abstractmethod
    def get_salary(self) -> float:
        pass

    @abstractmethod
    def get_tax(self) -> float:
        pass

    def __repr__(self):
        return (f"ID: {self.emp_id} | Прізвище: {self.surname:<12} | "
                f"ЗП: {self.get_salary():10.2f} | Податок: {self.get_tax():8.2f}")


class HourlyWorker(Employee):
    def __init__(self, emp_id: str, surname: str, rate: float, hours: float = None):
        super().__init__(emp_id, surname)
        self.rate = rate
        self.hours = hours if hours is not None else 20.8 * 8

    def get_salary(self) -> float:
        return self.hours * self.rate

    def get_tax(self) -> float:
        salary = self.get_salary()
        return salary * 0.18 + salary * 0.015


class FixedWorker(Employee):
    def __init__(self, emp_id: str, surname: str, salary: float):
        super().__init__(emp_id, surname)
        self.salary = salary

    def get_salary(self) -> float:
        return self.salary

    def get_tax(self) -> float:
        salary = self.get_salary()
        return salary * 0.18 + salary * 0.015


class FopWorker(Employee):
    def __init__(self, emp_id: str, surname: str, rate: float, group: int = 3, hours: float = None):
        super().__init__(emp_id, surname)
        self.rate = rate
        self.group = group
        self.hours = hours if hours is not None else 20.8 * 8

    def get_salary(self) -> float:
        return (self.hours * self.rate) * 1.10

    def get_tax(self) -> float:
        salary = self.get_salary()
        return salary * 0.05 + 1760.0


class ContractWorker(Employee):
    def __init__(self, emp_id: str, surname: str, price: float, lines: int):
        super().__init__(emp_id, surname)
        self.price = price
        self.lines = lines

    def get_salary(self) -> float:
        return self.price * self.lines

    def get_tax(self) -> float:
        salary = self.get_salary()
        return salary * 0.18 + salary * 0.015 + 1760.0


def create_workers(count: int = 20) -> list[Employee]:
    workers = []
    for i in range(1, count + 1):
        emp_id = f"ID{i:03d}"
        surname = fake.last_name()
        role = random.choice(['hourly', 'fixed', 'fop', 'contract'])

        if role == 'hourly':
            workers.append(HourlyWorker(emp_id, surname, random.randint(20, 60)))
        elif role == 'fixed':
            workers.append(FixedWorker(emp_id, surname, random.randint(25000, 80000)))
        elif role == 'fop':
            workers.append(FopWorker(emp_id, surname, random.randint(25, 70), group=random.choice([2, 3])))
        elif role == 'contract':
            workers.append(ContractWorker(emp_id, surname, round(random.uniform(0.5, 2.0), 2), random.randint(5000, 25000)))

    return workers


def sort_workers(workers: list[Employee]) -> list[Employee]:
    return sorted(workers, key=lambda w: (-w.get_salary(), w.surname))


WORKERS = create_workers(20)


@click.group()
def cli():
    pass


@cli.command(name="list")
def show_all():
    for w in sort_workers(WORKERS):
        click.echo(w)


@cli.command(name="filter-fop-group")
@click.option('--group', type=int, required=True)
def filter_fop_group(group):
    res = [w for w in WORKERS if isinstance(w, FopWorker) and w.group == group]
    for w in sort_workers(res):
        click.echo(w)


@cli.command(name="filter-income")
@click.option('--min-income', type=float, default=0.0)
@click.option('--max-income', type=float, default=float('inf'))
def filter_income(min_income, max_income):
    res = [w for w in WORKERS if min_income <= w.get_salary() <= max_income]
    for w in sort_workers(res):
        click.echo(w)


@cli.command(name="filter-taxes")
@click.option('--min-tax', type=float, default=0.0)
@click.option('--max-tax', type=float, default=float('inf'))
def filter_taxes(min_tax, max_tax):
    res = [w for w in WORKERS if min_tax <= w.get_tax() <= max_tax]
    for w in sort_workers(res):
        click.echo(w)


if __name__ == '__main__':
    cli()