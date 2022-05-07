from logging import ERROR
from logging.handlers import MemoryHandler


class CustomMemoryHandler(MemoryHandler):
    '''
    Memory handler is needed if a constant stream of logs is slowing down the software, for example
    in an HTTP logger where we want to flush once in a while all the logs. If all of them are sent
    in batch, a custom implementation in the handler should be done of the handle().
    '''

    def __init__(self,
                 capacity,
                 flushLevel=ERROR,
                 target=None,
                 flushOnClose=True,
                 batch_handle_buffer: bool = False,
                 ) -> None:
        super().__init__(capacity,
                         flushLevel,
                         target,
                         flushOnClose,
                         )
        self.batch_handle_buffer = batch_handle_buffer

    def emit(self, record):
        """
        Emit a record or append it to the buffer
        """
        if self.shouldFlush():
            self.flush()
        else:
            self.buffer.append(record)

    def shouldFlush(self):
        """
        Flush only when buffer is full
        """
        return len(self.buffer) >= self.capacity

    def flush(self) -> None:
        """
        Caches a number of logs in memory, and flushes all of them in one go.

        Example:
        capacity = 10
        memory_handler = CustomMemoryHandler(capacity,
                                             flushLevel=logging.WARNING,
                                             target=stream_handler)
        """
        self.acquire()
        try:
            if self.target:
                # Send to target all the logs or handle one by one
                if self.batch_handle_buffer:
                    self.target.handle(buffer)

                for log in self.buffer:
                    self.target.handle(log)

                self.buffer.clear()

        finally:
            self.release()
