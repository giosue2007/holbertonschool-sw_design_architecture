#!/usr/bin/env python3
"""
Factory pattern implementation with dynamic class registration.
"""
from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Abstract base class representing a generic vehicle."""

    @abstractmethod
    def mode(self) -> str:
        """Return the transit mode of the vehicle."""
        pass


class Bus(Vehicle):
    """Concrete vehicle implementation for Bus."""

    def mode(self) -> str:
        return "road"


class Train(Vehicle):
    """Concrete vehicle implementation for Train."""

    def mode(self) -> str:
        return "rails"


class Bike(Vehicle):
    """Concrete vehicle implementation for Bike."""

    def mode(self) -> str:
        return "lane"


class Scooter(Vehicle):
    """Concrete vehicle implementation for Scooter."""

    def mode(self) -> str:
        return "scooter_lane"


class VehicleFactory:
    """Factory managing vehicle instantiation through a registry."""

    def __init__(self) -> None:
        self._registry: dict[str, type[Vehicle]] = {}

    def register_kind(self, name: str, cls: type[Vehicle]) -> None:
        """Register a new vehicle type mapping."""
        self._registry[name] = cls

    def create(self, kind: str) -> Vehicle:
        """Instantiate a vehicle by its registered key name."""
        if kind not in self._registry:
            raise ValueError(f"Unknown vehicle kind: {kind}")
        return self._registry[kind]()


def main() -> None:
    """Main execution flow."""
    factory = VehicleFactory()
    factory.register_kind("bus", Bus)
    factory.register_kind("train", Train)
    factory.register_kind("bike", Bike)
    factory.register_kind("scooter", Scooter)

    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
