import os

class Config:
    CACHE_TYPE = os.getenv("CACHE_TYPE", "simple")
    
    CACHE_DEFAULT_TIMEOUT = int(os.getenv("CACHE_DEFAULT_TIMEOUT", 600))
