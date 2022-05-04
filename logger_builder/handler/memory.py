from logging.handlers import MemoryHandler


class CustomMemoryHandler(MemoryHandler):

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
                # Send to target all the list of logs, so that they are processed in batch
                self.target.handle(self.buffer)
                self.buffer.clear()
        finally:
            self.release()
