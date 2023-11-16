import click
from random import randint
from typing import Dict


class Pizza:
    def __init__(self, name, toppings):
        self.name = name
        self.toppings = toppings

    def dict(self) -> Dict[str, list]:
        return {self.name: self.toppings}

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.toppings == other.toppings


class PizzaOrder:

    @staticmethod
    def prepare_pizza(pizza, delivery=False):
        """ Приготовление пиццы и вывод времени приготовления и доставки"""
        if delivery:
            s = randint(1, 10)
            print(f"Prepared in {s}s")
            s = randint(1, 10)
            print(f"Delivered in {s}s")
        else:
            s = randint(1, 10)
            print(f"Prepared in {s}s")

    @staticmethod
    def display_menu(pizzas):
        for pizza in pizzas:
            toppings = ', '.join(pizzas[pizza])
            print(f"- {pizza}: {toppings}")


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', is_flag=True, help='Deliver the pizza')
@click.argument('pizza', nargs=1)
def order(pizza, delivery):
    """ Выполнение команды order, приготовление пиццы и ее доставка(если указан флаг)"""
    menu = {
        "Margherita": ["tomato sauce", "mozzarella", "tomatoes"],
        "Pepperoni": ["tomato sauce", "mozzarella", "pepperoni"],
        "Hawaiian": ["tomato sauce", "mozzarella", "chicken", "pineapples"]
    }
    if pizza in menu:
        selected_pizza = Pizza(pizza, menu[pizza])
        PizzaOrder.prepare_pizza(selected_pizza, delivery)
    else:
        print("This pizza is not in menu")


@cli.command()
def menu():
    """Выполнение команды order"""
    menu = {
        "Margherita ": ["tomato sauce", "mozzarella", "tomatoes"],
        "Pepperoni ": ["tomato sauce", "mozzarella", "pepperoni"],
        "Hawaiian ": ["tomato sauce", "mozzarella", "chicken", "pineapples"]
    }
    PizzaOrder.display_menu(menu)


if __name__ == '__main__':
    cli()
