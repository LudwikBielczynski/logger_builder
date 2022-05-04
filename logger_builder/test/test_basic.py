from logging import Logger
from unittest import TestCase


from logger_builder import LoggerBuilder


class TestBasicLogging(TestCase):
    '''Using TestCase functionality to catch logs'''

    def test_create_simple_logger(self):
        # Arrange
        logger_builder = LoggerBuilder([])
        logger_name = 'trial'

        # Act
        logger = logger_builder.create_logger(logger_name)

        assert type(logger) == Logger
        assert logger.name == logger_name
        assert logger.handlers == []
        assert logger.filters == []

    def test_simple_message(self):
        # Arrange
        logger_builder = LoggerBuilder([])
        logger_name = 'trial'
        logger = logger_builder.create_logger(logger_name)

        # Act
        message = 'Something'
        with self.assertLogs() as captured:
            logger.info(message)

        assert captured.output == [f'INFO:{logger_name}:{message}']
