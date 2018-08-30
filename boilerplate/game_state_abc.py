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
    def get_static_groups(self):
        pass

    @abstractmethod
    def get_collectable_groups(self):
        pass

    @abstractmethod
    def handle_events(self, event_list):
        pass

    def update(self, time_delta):
        """
        Call the update function for all of the groups.
        """
        for group in self.get_all_groups():
            group.update(self.get_static_groups(), 
                            self.get_collectable_groups(), time_delta)
