from slowapi import Limiter
from slowapi.util import get_remote_address

# api rate limiting
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["60/minute"],
    strategy='fixed-window-elastic-expiry',
)
