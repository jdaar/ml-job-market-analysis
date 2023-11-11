from abc import ABC, abstractmethod

class AbstractStrategy(ABC):
    @abstractmethod
    async def run() -> dict:
        raise NotImplementedError