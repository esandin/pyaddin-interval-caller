import call_later
import Tkinter

import pythonaddins

class TKEventLoop(object):
    _interval = 1
    def __init__(self):
        self._running = False
        self.start()
    def start(self):
        self._running = True
        call_later.call_later(self.tick, self._interval)
    def stop(self):
        self._running = False
    def tick(self):
        #while Tkinter.tkinter.dooneevent(Tkinter.tkinter.DONT_WAIT):
        #    pass
        pythonaddins._WriteStringToPythonWindow("Tick {}, {}".format(self._running, self._interval))
        if self._running:
            call_later.call_later(self.tick, self._interval)

tk_loop = TKEventLoop()