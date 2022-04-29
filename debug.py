from logger_builder import LoggerBuilder
from logger_builder.formatter import create_basic_formatter
from logger_builder.handler import StreamHandler

if __name__ == '__main__':
    formatter = create_basic_formatter()
    stream_handler = StreamHandler(formatter)

    handlers = [stream_handler]
    logger_builder = LoggerBuilder(handlers)
    logger = logger_builder.create_logger('trial')

    logger.info('Something')
