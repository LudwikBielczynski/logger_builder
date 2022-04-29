from abc import ABC, abstractmethod
from logging import Logger, Formatter, DEBUG, getLogger

from typing import TYPE_CHECKING, Sequence

from .handler import HandlerAbstract

if TYPE_CHECKING:
    from logging import Logger

class LoggerBuilderAbstract(ABC):


    @abstractmethod
    def create_logger(self, logger_name: str) -> Logger:
        '''Method implemented in concrete class returning a logger'''

class LoggerBuilder(LoggerBuilderAbstract):

    def __init__(self, handlers: Sequence[HandlerAbstract]) -> None:
        self.handlers = handlers

    def create_logger(self, logger_name: str) -> Logger:
        logger = getLogger(logger_name)
        logger.setLevel(DEBUG)
        for handler in self.handlers:
            logger = handler.add_handler(logger)

        return logger
