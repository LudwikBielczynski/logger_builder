import pytest

from logger_builder import LoggerBuilder
from logger_builder.formatter import create_formatter
from logger_builder.handler import CustomMemoryHandler
from logger_builder.handler.factory import FileHandlerFactory, MemoryHandlerFactory

MEMORY_LOGS_BUFFER_SIZE = 3


@pytest.fixture(autouse=True)
def logger_to_file_with_memory(tmp_path):
    formatter = create_formatter()
    logger_name = 'logger_to_file'
    file_handler_factory = FileHandlerFactory(tmp_path, logger_name, formatter)

    memory_handler_factory = MemoryHandlerFactory(
        file_handler_factory, MEMORY_LOGS_BUFFER_SIZE)

    handlers = [memory_handler_factory]
    logger_builder = LoggerBuilder(handlers)
    logger_name = 'logger_file'

    logger = logger_builder.create_logger(logger_name)

    return logger


def test_attached_memory_handler(logger_to_file_with_memory):
    assert type(logger_to_file_with_memory.handlers[0]) == CustomMemoryHandler


def test_basic_stream_output_with_memory_handler(logger_to_file_with_memory, caplog, tmp_path):
    # Arrange
    def get_logs(tmp_path):
        log_files = list(tmp_path.iterdir())
        with open(log_files[0]) as log_file:
            logs_in_file = log_file.readlines()
        return logs_in_file

    # Act
    message = 'Something'
    logger_to_file_with_memory.info(message)
    logs_in_file = get_logs(tmp_path)
    assert len(logs_in_file) == 0

    for _ in range(0, 5):
        logger_to_file_with_memory.info(message)

    logs_in_file = get_logs(tmp_path)
    assert len(logs_in_file) == MEMORY_LOGS_BUFFER_SIZE
