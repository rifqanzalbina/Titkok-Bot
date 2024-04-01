from art import *
from typing import Self

class MyLock:
    def __enter__(self) -> Self:
        self.lock()
        return self
    
tprint("Tiktok Bot")
