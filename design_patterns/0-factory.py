#!/usr/bin/env python3
"""Module implementing the Vehicle Factory Pattern using a registry."""


class Vehicle:
    """Interface / Base class for all vehicles."""

    def mode(self) -> str:
        """Returns the mode of travel."""
        pass


class Bus(Vehicle):
    """Concrete Vehicle: Bus."""

    def mode(self) -> str:
        return "road"


class Train(Vehicle):
    """Concrete Vehicle: Train."""

    def mode(self) -> str:
        return "rails"


class Bike(Vehicle):
    """Concrete Vehicle: Bike."""

    def mode(self) -> str:
        return "lane"


class Scooter(Vehicle):
    """Concrete Vehicle: Scooter (New type to register)."""

    def mode(self) -> str:
        return "scooter_lane"


class VehicleFactory:
    """Factory class that centralizes vehicle creation via a registry."""

    def __init__(self):
        """Initializes the factory with an empty registry dictionary."""
        self._registry = {}

    def register_kind(self, name: str, cls):
        """Registers a new vehicle class under a specific string name."""
        self._registry[name] = cls

    def create(self, kind: str) -> Vehicle:
        """Creates an instance of a registered vehicle type."""
        if kind not in self._registry:
            raise ValueError(f"Unknown vehicle kind: {kind}")
        return self._registry[kind]()


def main():
    """Main execution function."""
    factory = VehicleFactory()

    # Initial registration of default vehicles
    factory.register_kind("bus", Bus)
    factory.register_kind("train", Train)
    factory.register_kind("bike", Bike)

    # TASK: Registering the new vehicle type without modifying the factory
    factory.register_kind("scooter", Scooter)

    # Printing outputs
    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
