import os
import sys
import time
import queue
import random

request_queue = queue.Queue()


def generate_request():
    request_id = random.randint(1000, 9999)
    print(f"Homework 2 - Task 1 | Request ID={request_id} | Generating request")
    request_queue.put(request_id)
    print(f"Homework 2 - Task 1 | Request ID={request_id} | Add a request to the queue")


def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Homework 2 - Task 1 | Request ID={request_id} | Request processing")
    else:
        print(f"Homework 2 - Task 1 | The queue is empty")


def main():
    while True:
        generate_request()
        process_request()
        time.sleep(1)


if __name__ == "__main__":
    try:
        print(f"Homework 2 - Task 1 | Starting processing requests")
        main()
    except KeyboardInterrupt:
        print(f"\nHomework 2 - Task 1 | Good bye!")
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
