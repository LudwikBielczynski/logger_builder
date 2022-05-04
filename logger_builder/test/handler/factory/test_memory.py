import logging.handlers

import pytest

from logger_builder import LoggerBuilder
from logger_builder.formatter import create_formatter
from logger_builder.handler import CustomMemoryHandler
from logger_builder.handler.factory import StreamHandlerFactory, MemoryHandlerFactory


@pytest.fixture(autouse=True)
def logger_stream_with_memory():
    formatter = create_formatter()
    stream_handler_factory = StreamHandlerFactory(formatter)
    memory_handler_factory = MemoryHandlerFactory(stream_handler_factory, 4)

    handlers = [memory_handler_factory]
    logger_builder = LoggerBuilder(handlers)
    logger_name = 'logger_stream'

    logger = logger_builder.create_logger(logger_name)

    return logger


def test_attached_memory_handler(logger_stream_with_memory):
    assert type(logger_stream_with_memory.handlers[0]) == CustomMemoryHandler


def test_basic_stream_output_with_memory_handler(logger_stream_with_memory, caplog):
    # Act
    message = 'Something'
    logger_stream_with_memory.info(message)

    assert len(caplog.records) == 0

    for _ in range(0, 5):
        logger_stream_with_memory.info(message)
    assert len(caplog.records) == 4
