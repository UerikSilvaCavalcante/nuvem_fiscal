from abc import ABC, abstractmethod
from typing import List, Generic, TypeVar

T = TypeVar("T")


class PayloadSerializer(ABC, Generic[T]):
    @abstractmethod
    def serialize(self) -> T:
        pass
