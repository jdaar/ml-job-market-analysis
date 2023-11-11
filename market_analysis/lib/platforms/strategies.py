from enum import Enum

from .base_strategy import AbstractStrategy

class LinkedinStrategy(AbstractStrategy):
    @staticmethod
    async def run(url) -> dict:
        print(url)
        return {}

class Platforms(Enum):
    Linkedin = "linkedin"

PlatformStrategies = {
    Platforms.Linkedin: LinkedinStrategy,
}