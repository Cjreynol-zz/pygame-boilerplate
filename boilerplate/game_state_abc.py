from abc import ABC, abstractmethod


class GameStateABC(ABC):
    """
    Set up the expected interface for specific game states to work in my 
    boilerplate framework.
    """

    def __init__(self):
        self.done = False

    @abstractmethod
    def get_all_groups(self):
        pass

    @abstractmethod
    def get_collide_groups(self):
        pass

    def update(self):
        for group in self.get_all_groups():
            group.update(self.get_collide_groups())
