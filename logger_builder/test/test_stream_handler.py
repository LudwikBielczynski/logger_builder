import logging
from unittest import TestCase

import pytest

from logger_builder import LoggerBuilder
from logger_builder.formatter import create_basic_formatter
from logger_builder.handler import StreamHandler

@pytest.fixture(autouse=True)
def logger_stream():
    formatter = create_basic_formatter()
    stream_handler = StreamHandler(formatter)

    handlers = [stream_handler]
    logger_builder = LoggerBuilder(handlers)
    logger_name = 'logger_stream'

    logger = logger_builder.create_logger(logger_name)

    return logger

def test_attached_stream_handler(logger_stream):
    assert type(logger_stream.handlers[0]) == logging.StreamHandler

def test_basic_stream_output(logger_stream, caplog):
    # Act
    message = 'Something'
    logger_stream.info(message)

    assert caplog.records[0].message == message
