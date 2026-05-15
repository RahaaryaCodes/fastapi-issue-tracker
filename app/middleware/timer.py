import time
from fastapi import Request


async def timer_middleware(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    response.headers["X-Process-Time"] = f"{process_time:.4f}s"

    print(f"Request processed in {process_time:.4f} seconds")

    return response
