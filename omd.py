import click
from Pizza import Pizza
from decorator import log


@log('Пицца приготовится за')
def bake(pizza: Pizza) -> None:
    """ Пицца готовится """
    pass


@log('Доставим пиццу за')
def deliver(pizza: Pizza) -> None:
    """ Пицца доставляется"""
    pass


def display_menu(pizzas: dict):
    for pizza in pizzas:
        toppings = ', '.join(pizzas[pizza])
        print(f"- {pizza}: {toppings}")


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', is_flag=True, help='Deliver the pizza')
@click.option('--size', default='L', help='Pizza size (L/XL)')
@click.argument('pizza', nargs=1)
def order(pizza: Pizza, delivery: bool):
    """
    Выполнение команды order,
    приготовление пиццы и ее доставка(если указан флаг)
    """
    menu = {
        "Margherita": ["tomato sauce", "mozzarella", "tomatoes"],
        "Pepperoni": ["tomato sauce", "mozzarella", "pepperoni"],
        "Hawaiian": ["tomato sauce", "mozzarella", "chicken", "pineapples"]
    }
    if pizza in menu:
        selected_pizza = Pizza(pizza, menu[pizza])
        bake(selected_pizza)
        if delivery:
            deliver(selected_pizza)

    else:
        print("This pizza is not in menu")


@cli.command()
def menu():
    """Выполнение команды menu"""
    menu = {
        "Margherita ": ["tomato sauce", "mozzarella", "tomatoes"],
        "Pepperoni ": ["tomato sauce", "mozzarella", "pepperoni"],
        "Hawaiian ": ["tomato sauce", "mozzarella", "chicken", "pineapples"]
    }
    display_menu(menu)


if __name__ == '__main__':
    cli()

