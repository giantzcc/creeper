# -*- coding: utf-8 -*-
import threading
class LoopTimer(threading.Timer):
    def __init__(self, interval, function, args=[], kwargs={}):
        super(LoopTimer,self).__init__(interval, function, args, kwargs)

    def run(self):
        while True:
            self.finished.wait(self.interval)
            if self.finished.is_set():
                self.finished.set()
                break
            self.function(*self.args, **self.kwargs)