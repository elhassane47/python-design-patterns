from abc import ABC, abstractmethod
from collections import defaultdict
from random import randrange
from typing import List


class Subject(ABC):

    @abstractmethod
    def subscribe(self, observer):
        pass

    @abstractmethod
    def unsubscribe(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class Observer(ABC):

    @abstractmethod
    def notify(self, subject):
        pass


class ConcreteSubject(Subject):

    def __init__(self):
        self._observers: List[Observer] = []
        self._state = 0

    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.notify(self)

    def some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """
        self._state = randrange(0, 10)
        self.notify_observers()


class ConcreteObserverA(Observer):
    def notify(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def notify(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")


##################################### Using Dicts ###############################################

subscribers = defaultdict(list)

USER_REGISTRED = "user_registered"
PASSWORD_FORGOTTEN = "user_password_forgotten"

def subscribe(event_type, fn):
    subscribers[event_type].append(fn)


def post_event(event_type, data):
    for fn in subscribers[event_type]:
        fn(data)


def handle_user_registered_event(user):
    print("handle_user_registered_event")


def handle_user_password_forgotten_event(user):
    print("handle_user_password_forgotten_event")


def setup_email_event_handlers():
    subscribe(USER_REGISTRED, handle_user_registered_event)
    subscribe(PASSWORD_FORGOTTEN, handle_user_password_forgotten_event)


class User:

    @classmethod
    def register_new_user(self, name: str, password: str, email: str):
        print("register new user")
        post_event(USER_REGISTRED, self)

    def password_forgotten(self, email: str):
        print("password forgotten")
        post_event(PASSWORD_FORGOTTEN, self)


if __name__ == "__main__":

    sub = ConcreteSubject()
    obs1 = ConcreteObserverA()
    obs2 = ConcreteObserverB()
    sub.subscribe(obs2)
    sub.subscribe(obs1)
    sub.some_business_logic()

    setup_email_event_handlers()
    User.register_new_user("hassane","password", "email")


