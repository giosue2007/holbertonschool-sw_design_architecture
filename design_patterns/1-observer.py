#!/usr/bin/env python3
"""
Observer pattern implementation with topic filtering.
"""
from abc import ABC, abstractmethod
from typing import Optional, Set, Dict


class Observer(ABC):
    """Abstract base class for all observers."""

    @abstractmethod
    def update(self, topic: str, data: str) -> None:
        """Receive notification from subject."""
        pass


class NewsSubject:
    """Subject that manages subscribers and notifies them of events."""

    def __init__(self) -> None:
        self._observers: Dict[Observer, Optional[Set[str]]] = {}

    def subscribe(
        self, observer: Observer, topics: Optional[Set[str]] = None
    ) -> None:
        """Subscribe an observer, optionally filtering by specific topics."""
        self._observers[observer] = topics

    def unsubscribe(self, observer: Observer) -> None:
        """Unsubscribe an observer."""
        self._observers.pop(observer, None)

    def notify(self, topic: str, data: str) -> None:
        """Notify registered observers if they subscribed to the topic."""
        for observer, topics in list(self._observers.items()):
            if topics is None or topic in topics:
                observer.update(topic, data)


class LogObserver(Observer):
    """Concrete observer logging events."""

    def update(self, topic: str, data: str) -> None:
        print(f"log:{topic}={data}")


class EmailObserver(Observer):
    """Concrete observer sending email notifications."""

    def update(self, topic: str, data: str) -> None:
        print(f"email:{topic}={data}")


class SmsObserver(Observer):
    """Concrete observer sending SMS alerts."""

    def update(self, topic: str, data: str) -> None:
        print(f"sms:{topic}={data}")


def main() -> None:
    """Main execution flow."""
    subject = NewsSubject()

    log_obs = LogObserver()
    email_obs = EmailObserver()
    sms_obs = SmsObserver()

    subject.subscribe(log_obs, topics={"sports", "breaking"})
    subject.subscribe(email_obs)
    subject.subscribe(sms_obs, topics={"breaking"})

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
