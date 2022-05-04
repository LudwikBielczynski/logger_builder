from abc import ABC, abstractmethod
from logging import DEBUG, Logger


class HandlerAbstract(ABC):

    @abstractmethod
    def add_handler(self, logger: Logger, logging_level: int = DEBUG) -> Logger:
        ...
