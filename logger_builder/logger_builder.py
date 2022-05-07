from abc import ABC, abstractmethod
from logging import Logger, DEBUG, getLogger
# from typing import

from .handler.factory import HandlerFactoryAbstract


class LoggerBuilderAbstract(ABC):
    """
    Logger builder has a stepwise attachment of handlers implemented. The handlers are attached
    through the handler factories which has an add_handler function implemented.
    """
    def __init__(self, handler_factories: set[HandlerFactoryAbstract]) -> None:
        self._handler_factories = handler_factories

    def reset(self) -> None:
        """
        At this moment it is only emptying the set of handler factories
        """
        # TODO: In future a destructor should be implemented as well for the reset step, as logger
        # in logging is a singleton, so emptying factories won't mean that a logger of the same
        # name fetched by the logging.get_logger() won't have all the previous formatters handlers
        # etc.
        self._handler_factories = set()

    @abstractmethod
    def create_logger(self, logger_name: str, logging_level: int = DEBUG) -> Logger:
        """Method implemented in concrete class returning a logger"""


class LoggerBuilder(LoggerBuilderAbstract):
    def create_logger(self, logger_name: str, logging_level: int = DEBUG) -> Logger:
        logger = getLogger(logger_name)
        logger.setLevel(logging_level)

        for handler in self._handler_factories:
            logger = handler.add_handler(logger)

        return logger
