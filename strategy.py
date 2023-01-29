from abc import abstractmethod, ABC
import random
from typing import List


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def create_ordering(self, data: List) -> List:
        pass


class RandomOrderingStrategy(Strategy):
    def create_ordering(self, data: List) -> List:
        list_copy = data.copy()
        random.shuffle(list_copy)
        return list_copy


class AlphabeticOrderingStrategy(Strategy):
    def create_ordering(self, data: List) -> List:
        list_copy = data.copy()
        return sorted(list_copy)


class Context:

    def __init__(self, strategy:Strategy) -> None:
        self._strategy = strategy

    def strategy(self) -> Strategy:
        return self._strategy

    def set_strategy(self, strategy:Strategy) -> None:
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """

        # ...

        result = self._strategy.create_ordering(["a", "b", "c", "d", "e"])
        print(",".join(result))


if __name__ == "__main__":
    # The client code picks a concrete strategy and passes it to the context.
    # The client should be aware of the differences between strategies in order
    # to make the right choice.

    context = Context(RandomOrderingStrategy())
    print("Client: Random ordering.")
    context.do_some_business_logic()
    print()

    print("Client: Alphabetic ordering.")
    context.set_strategy(AlphabeticOrderingStrategy())
    context.do_some_business_logic()
