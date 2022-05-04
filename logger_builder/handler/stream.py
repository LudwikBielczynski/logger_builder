from logging import DEBUG, Formatter, Logger, StreamHandler as StreamHandlerLogging
import sys

from .abstract import HandlerAbstract


class StreamHandler(HandlerAbstract):

    def __init__(self, formatter: Formatter) -> None:
        self.formatter = formatter

    def add_handler(self, logger: Logger, logging_level: int = DEBUG) -> Logger:
        stream_handler = StreamHandlerLogging(sys.stdout)

        stream_handler.setLevel(logging_level)
        stream_handler.setFormatter(self.formatter)

        logger.addHandler(stream_handler)

        return logger
