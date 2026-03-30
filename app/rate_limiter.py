import time

RATE_LIMIT = 5   # max requests
WINDOW = 60      # seconds

user_requests = {}

def check_rate_limit(user_id):
    now = time.time()

    if user_id not in user_requests:
        user_requests[user_id] = []

    # remove old requests
    user_requests[user_id] = [
        t for t in user_requests[user_id] if now - t < WINDOW
    ]

    if len(user_requests[user_id]) >= RATE_LIMIT:
        return False

    user_requests[user_id].append(now)
    return True