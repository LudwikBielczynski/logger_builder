import logging

from logger_builder.test.handler.fixtures import logger_stream

def test_attached_stream_handler(logger_stream):
    assert type(logger_stream.handlers[0]) == logging.StreamHandler

def test_basic_stream_output(logger_stream, caplog):
    # Act
    message = 'Something'
    logger_stream.info(message)

    assert caplog.records[0].message == message
