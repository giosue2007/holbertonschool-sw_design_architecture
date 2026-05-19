#!/usr/bin/env python3
"""Module implementing the Decorator Pattern for a coffee shop system."""


class Beverage:
    """Interface / Base class for all beverages."""

    def cost(self) -> int:
        """Returns the cost of the beverage."""
        pass

    def description(self) -> str:
        """Returns the description of the beverage."""
        pass


class Coffee(Beverage):
    """Concrete Beverage: Coffee."""

    def cost(self) -> int:
        return 50

    def description(self) -> str:
        return "Coffee"


class BeverageDecorator(Beverage):
    """Base Decorator class that wraps a Beverage."""

    def __init__(self, inner: Beverage) -> None:
        """Initializes the decorator with an inner beverage."""
        self._inner = inner

    def cost(self) -> int:
        return self._inner.cost()

    def description(self) -> str:
        return self._inner.description()


class MilkDecorator(BeverageDecorator):
    """Concrete Decorator: Adds milk to the beverage."""

    def cost(self) -> int:
        return self._inner.cost() + 10

    def description(self) -> str:
        return self._inner.description() + " + milk"


class SugarDecorator(BeverageDecorator):
    """Concrete Decorator: Adds sugar to the beverage."""

    def cost(self) -> int:
        return self._inner.cost() + 5

    def description(self) -> str:
        return self._inner.description() + " + sugar"


class CaramelDecorator(BeverageDecorator):
    """Concrete Decorator: Adds caramel to the beverage (Task)."""

    def cost(self) -> int:
        """Returns inner beverage cost plus caramel cost (15)."""
        return self._inner.cost() + 15

    def description(self) -> str:
        """Returns inner beverage description plus caramel text."""
        return self._inner.description() + " + caramel"


def main() -> None:
    """Main execution function."""
    # 1. Base coffee with milk
    milk_coffee = MilkDecorator(Coffee())
    print(f"{milk_coffee.description()} {milk_coffee.cost()}")

    # 2. Coffee with sugar and milk
    sugar_milk_coffee = MilkDecorator(SugarDecorator(Coffee()))
    print(f"{sugar_milk_coffee.description()} {sugar_milk_coffee.cost()}")

    # 3. TASK: Coffee with sugar, milk, and caramel
    fancy_coffee = CaramelDecorator(MilkDecorator(SugarDecorator(Coffee())))
    print(f"{fancy_coffee.description()} {fancy_coffee.cost()}")


if __name__ == "__main__":
    main()
