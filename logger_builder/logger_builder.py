from abc import ABC, abstractmethod
from logging import Logger, DEBUG, getLogger
from typing import Sequence

from .handler import HandlerAbstract


class LoggerBuilderAbstract(ABC):
    def __init__(self, handlers: Sequence[HandlerAbstract]) -> None:
        self._handlers = handlers

    def reset(self) -> None:
        self._handlers = []

    @abstractmethod
    def create_logger(self, logger_name: str, logging_level: int = DEBUG) -> Logger:
        """Method implemented in concrete class returning a logger"""


class LoggerBuilder(LoggerBuilderAbstract):
    def create_logger(self, logger_name: str, logging_level: int = DEBUG) -> Logger:
        logger = getLogger(logger_name)
        logger.setLevel(logging_level)

        for handler in self._handlers:
            logger = handler.add_handler(logger)

        return logger
