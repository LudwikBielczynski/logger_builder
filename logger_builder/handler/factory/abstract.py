from abc import ABC, abstractmethod
from logging import DEBUG, Logger, Handler


class HandlerFactoryAbstract(ABC):
    """
    A class holding create_handler which is a factory method. add_handler() is used by the builder
    to add the handler to the logger.
    """

    @abstractmethod
    def create_handler(self,
                       logging_level: int = DEBUG
                       ) -> Handler:
        ...

    @abstractmethod
    def add_handler(self, logger: Logger, logging_level: int = DEBUG) -> Logger:
        ...
