import time
from datetime import date
import datetime


def times():
    seconds = time.time()
    local=time.ctime(seconds)
    return local

def dates():
    cur = date.today()
    return cur




