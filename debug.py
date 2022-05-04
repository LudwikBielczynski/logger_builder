from logging import DEBUG
from pathlib import Path

from logger_builder import LoggerBuilder
from logger_builder.formatter import create_formatter
from logger_builder.handler.factory import (StreamHandlerFactory,
                                            FileHandlerFactory,
                                            MemoryHandlerFactory,
                                            )

if __name__ == "__main__":
    formatter = create_formatter(simple_description=True)

    log_file_path = Path("~/Downloads").expanduser()
    file_handler_factory = FileHandlerFactory(log_file_path, 'trial', formatter)

    stream_handler_factory = StreamHandlerFactory(formatter)

    memory_handler_factory = MemoryHandlerFactory(file_handler_factory, 3)


    handler_factories = [stream_handler_factory, memory_handler_factory]
    logger_builder = LoggerBuilder(handler_factories)
    logger = logger_builder.create_logger("trial")

    for log_nr in range(0, 6):
        logger.info(f"Something {log_nr}")
