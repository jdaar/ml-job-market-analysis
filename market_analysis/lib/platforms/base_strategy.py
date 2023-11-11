from abc import ABC, abstractmethod


class AbstractStrategy(ABC):
    @abstractmethod
    async def run(line: dict) -> dict:
        raise NotImplementedError
