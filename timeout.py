#!/usr/bin/env python

class TimeExceededError(Exception):pass
def run_cmd(cmd, timeout = 0):
    import signal
    def alarmHandler(signum, frame):
        raise TimeExceededError("Took too long to execute")
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(1)

    cmd()


def myfunc():
    import time
    time.sleep(2)
    return

try:
    run_cmd(myfunc, 50000)
except TimeExceededError:
    print("Function timed out!")