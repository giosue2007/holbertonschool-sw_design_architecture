#!/usr/bin/env python3
"""Module implementing the Observer Pattern for a news notification system."""


class Observer:
    """Interface / Base class for all observers."""

    def update(self, topic: str, data: str) -> None:
        """Receive an update notification from the subject."""
        pass


class NewsSubject:
    """The Subject (Publisher) that broadcasts news to subscribers."""

    def __init__(self) -> None:
        """Initializes the subject with an empty dictionary of observers."""
        self._observers: dict = {}

    def subscribe(self, observer: Observer, topics: set = None) -> None:
        """Subscribes an observer to specific topics or all topics if None."""
        self._observers[observer] = topics

    def unsubscribe(self, observer: Observer) -> None:
        """Removes an observer from the subscription dictionary."""
        if observer in self._observers:
            del self._observers[observer]

    def notify(self, topic: str, data: str) -> None:
        """Notifies all interested observers about an event."""
        # Snapshot iteration (list(self._observers.items())) handles safe modification
        for obs, topics in list(self._observers.items()):
            if topics is None or topic in topics:
                obs.update(topic, data)


class LogObserver(Observer):
    """Concrete Observer that logs specific topics."""

    def update(self, topic: str, data: str) -> None:
        print(f"log:{topic}={data}")


class EmailObserver(Observer):
    """Concrete Observer that sends emails for all topics."""

    def update(self, topic: str, data: str) -> None:
        print(f"email:{topic}={data}")


class SmsObserver(Observer):
    """Concrete Observer that sends SMS alerts for urgent news (Task)."""

    def update(self, topic: str, data: str) -> None:
        """Prints the SMS notification format."""
        print(f"sms:{topic}={data}")


def main() -> None:
    """Main execution function."""
    subject = NewsSubject()

    log_obs = LogObserver()
    email_obs = EmailObserver()
    sms_obs = SmsObserver()

    # Subscribing existing observers
    subject.subscribe(log_obs, topics={"sports", "breaking"})
    subject.subscribe(email_obs, topics=None)  # None means all topics

    # TASK: Subscribe the new SmsObserver only to "breaking" news
    subject.subscribe(sms_obs, topics={"breaking"})

    # Simulating events
    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
 