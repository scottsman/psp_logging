import time

class Process(object):
    """ A single process.

    Attributes:
        start_time
        end_time
        name
    """
    def __init__(self, name, start_time=None, end_time=None):
        """
        Args:
            name (str): Name of the process.
        Kwargs:
            start_time (float): Manual entry for a start time, in epoch time.
            end_time (float): Manual entry for an end time, in epoch time.
        """
        self._name = name
        self._start_time = start_time or time.time()
        self._end_time = end_time or None

    @property
    def name(self):
        """
        """
        return self.name

    @property
    def start_time(self):
        """ 
        """
        return time.ctime(self._start_time)

    @property
    def end_time(self):
        """
        """
        if self._end_time:
            return time.ctime(self._end_time)

