#!/usr/bin/env python3
"""
Decorator pattern implementation for dynamic beverage composition.
"""
from abc import ABC, abstractmethod


class Beverage(ABC):
    """Abstract base class for all beverages and decorators."""

    @abstractmethod
    def cost(self) -> int:
        """Return the total cost of the beverage."""
        pass

    @abstractmethod
    def description(self) -> str:
        """Return the description of the beverage."""
        pass


class Coffee(Beverage):
    """Base concrete beverage component."""

    def cost(self) -> int:
        return 50

    def description(self) -> str:
        return "Coffee"


class MilkDecorator(Beverage):
    """Decorator adding milk to a beverage (+10 cents)."""

    def __init__(self, inner: Beverage) -> None:
        self._inner = inner

    def cost(self) -> int:
        return self._inner.cost() + 10

    def description(self) -> str:
        return self._inner.description() + " + milk"


class SugarDecorator(Beverage):
    """Decorator adding sugar to a beverage (+5 cents)."""

    def __init__(self, inner: Beverage) -> None:
        self._inner = inner

    def cost(self) -> int:
        return self._inner.cost() + 5

    def description(self) -> str:
        return self._inner.description() + " + sugar"


class CaramelDecorator(Beverage):
    """Decorator adding caramel to a beverage (+15 cents)."""

    def __init__(self, inner: Beverage) -> None:
        self._inner = inner

    def cost(self) -> int:
        return self._inner.cost() + 15

    def description(self) -> str:
        return self._inner.description() + " + caramel"


def main() -> None:
    """Main execution flow."""
    # Café de base + Lait
    coffee_milk = MilkDecorator(Coffee())
    print(f"{coffee_milk.description()} {coffee_milk.cost()}")

    # Café + Sucre + Lait
    coffee_sugar_milk = MilkDecorator(SugarDecorator(Coffee()))
    print(f"{coffee_sugar_milk.description()} {coffee_sugar_milk.cost()}")

    # Café + Sucre + Lait + Caramel
    coffee_full = CaramelDecorator(MilkDecorator(SugarDecorator(Coffee())))
    print(f"{coffee_full.description()} {coffee_full.cost()}")


if __name__ == "__main__":
    main()
