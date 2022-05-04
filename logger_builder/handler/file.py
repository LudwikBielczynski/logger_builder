from datetime import datetime
from logging import DEBUG, Formatter, Logger, FileHandler as FileHandlerLogging
from typing import TYPE_CHECKING

from .abstract import HandlerAbstract

if TYPE_CHECKING:
    from pathlib import Path


class FileHandler(HandlerAbstract):

    def __init__(self,
                 log_file_path: 'Path',
                 formatter: Formatter
                 ) -> None:
        self.log_file_path = log_file_path
        self.formatter = formatter

    def add_handler(self, logger: Logger, logging_level: int = DEBUG) -> Logger:
        file_name = f'{datetime.now().date()}_{logger.name}.log'
        file_handler = FileHandlerLogging(self.log_file_path / file_name)

        file_handler.setLevel(logging_level)
        file_handler.setFormatter(self.formatter)

        logger.addHandler(file_handler)

        return logger
