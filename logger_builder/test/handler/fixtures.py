import pytest

from logger_builder import LoggerBuilder
from logger_builder.formatter import create_formatter
from logger_builder.handler import StreamHandler

@pytest.fixture(autouse=True)
def logger_stream():
    formatter = create_formatter()
    stream_handler = StreamHandler(formatter)

    handlers = [stream_handler]
    logger_builder = LoggerBuilder(handlers)
    logger_name = 'logger_stream'

    logger = logger_builder.create_logger(logger_name)

    return logger