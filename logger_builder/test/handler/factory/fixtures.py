import pytest

from logger_builder import LoggerBuilder
from logger_builder.formatter import create_formatter
from logger_builder.handler.factory import StreamHandlerFactory

@pytest.fixture(autouse=True)
def logger_stream():
    formatter = create_formatter()
    stream_handler_factory = StreamHandlerFactory(formatter)

    handler_factories = [stream_handler_factory]
    logger_builder = LoggerBuilder(handler_factories)
    logger_name = 'logger_stream'

    logger = logger_builder.create_logger(logger_name)

    return logger