from abc import ABC, abstractmethod
from typing import List


class Sensor(ABC):

    @abstractmethod
    def listen_sensor(self):
        pass


class Subscriber(ABC):

    @abstractmethod
    def update(self, context):
        pass

class SubscriptionManager(ABC):

    @abstractmethod
    def subscribe(self, sub: Subscriber):
        pass
    
    @abstractmethod
    def unsubscribe(self, sub: Subscriber):
        pass
    
    @abstractmethod
    def notify(self, context):
        pass


class OutdoorSensorSub(Subscriber):
    """ Test subscriber """
    _state: bool

    def update(self, context):
        if isinstance(context, bool):
            _state = context
            print("\nNew state --->", context, "\n")
            return context
        return None

class SubscribersManager(SubscriptionManager):
    _subscribers:List[Subscriber] = []

    def subscribe(self, sub: Subscriber):
        self._subscribers.append(sub)
        print("====> Added new subscriber", sub)
    
    def unsubscribe(self, sub: Subscriber):
        self._subscribers.remove(sub)
    
    def notify(self, context):
        for sub in self._subscribers:
            sub.update(context)