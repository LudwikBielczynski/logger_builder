from logging import DEBUG, Logger, Handler

from logger_builder.handler import CustomMemoryHandler
from .abstract import HandlerFactoryAbstract


class MemoryHandlerFactory(HandlerFactoryAbstract):
    """
    Factory used to create a memory handler. It needs a different memory handler factory which will
    be passed as an attribute. This target handler will be buffered by the memory handler.
    """

    def __init__(self,
                 target_handler_factory: HandlerFactoryAbstract,
                 logging_buffer_size: int = 5,
                 ) -> None:
        self.target_handler_factory = target_handler_factory
        self.logging_buffer_size = logging_buffer_size

    def create_handler(self,
                       logging_level: int = DEBUG
                       ) -> CustomMemoryHandler:

        target_handler = self.target_handler_factory.create_handler()
        memory_handler = CustomMemoryHandler(self.logging_buffer_size,
                                             logging_level,
                                             target_handler,
                                             )

        return memory_handler

    def add_handler(self, logger: Logger, logging_level: int = DEBUG) -> Logger:
        memory_handler = self.create_handler(logging_level)
        logger.addHandler(memory_handler)
        return logger
