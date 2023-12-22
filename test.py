import pytest
from pizza import Pizza


class TestPizza:
    def test_size(self):
        pizza = Pizza("Margherita ",
                      ["tomato sauce", "mozzarella", "tomatoes"])
        assert pizza.size == 'L'

    def test_XL_size(self):
        pizza = Pizza("Margherita ",
                      ["tomato sauce", "mozzarella", "tomatoes"], 'XL')
        assert pizza.size == 'XL'

    def test_wrong_size(self):
        with pytest.raises(TypeError):
            Pizza(size=230)

    def test_eq(self):
        pizza1 = Pizza("Margherita ",
                       ["tomato sauce", "mozzarella", "tomatoes"], 'XL')
        pizza2 = Pizza("Margherita ",
                       ["tomato sauce", "mozzarella", "tomatoes"], 'XL')
        assert pizza1 == pizza2

    def test_different_pizzas(self):
        pizza1 = Pizza("Margherita ",
                       ["tomato sauce", "mozzarella", "tomatoes"], 'XL')
        pizza2 = Pizza("Pepperoni ",
                       ["tomato sauce", "mozzarella", "pepperoni"], 'L')
        assert pizza1 != pizza2


if __name__ == '__main__':
    pytest.main()
