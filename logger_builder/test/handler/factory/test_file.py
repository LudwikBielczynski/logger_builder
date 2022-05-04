import logging

import pytest

from logger_builder import LoggerBuilder
from logger_builder.formatter import create_formatter
from logger_builder.handler.factory import FileHandlerFactory


@pytest.fixture(autouse=True)
def logger_to_file(tmp_path):
    formatter = create_formatter()
    logger_name = 'logger_to_file'
    file_handler_factory = FileHandlerFactory(tmp_path, logger_name, formatter)

    handler_factories = [file_handler_factory]
    logger_builder = LoggerBuilder(handler_factories)

    logger = logger_builder.create_logger(logger_name)

    return logger


def test_attached_file_handler(logger_to_file):
    assert type(logger_to_file.handlers[0]) == logging.FileHandler


def test_log_file_present(logger_to_file, tmp_path):
    # Act
    message = 'Something'
    logger_to_file.info(message)

    # Assert
    log_files = list(tmp_path.iterdir())
    assert len(log_files) == 1


def test_basic_stream_output(logger_to_file, tmp_path):
    # Act
    message_to_log = 'Something'
    logger_to_file.info(message_to_log)

    # Assert
    log_files = list(tmp_path.iterdir())
    with open(log_files[0]) as log_file:
        logs_in_file = log_file.readlines()

    assert len(logs_in_file) == 1
    message_logged = logs_in_file[0] \
        .split(' ')[-1] \
        .split('\n')[0]
    assert message_logged == message_to_log
