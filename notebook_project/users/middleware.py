import logging
import time

logger = logging.getLogger(__name__)

class SampleMiddleware:
    def __init__(self, get_request):
        self.get_request = get_request

        # server啟動時，僅執行一次
        logger.info("LoggingMiddleware initialized.")

    def __call__(self, request):
        # veiw處理前
        start = time.time()
        logger.info(f"Request start: {request.path}, from <{request.user}>")

        responce = self.get_request(request)

        # veiw處理後
        duration = time.time() - start
        logger.info(f"Request end: {request.path}, took {duration:.2f}s")

        return responce