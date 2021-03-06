import time

class Process(object):
    """ A single process.

    Attributes:
        start_time
        stop_time
        name
    """

    def __init__(self, name, start_time=None, stop_time=None):
        """
        Args:
            name (str): Name of the process.
        Kwargs:
            start_time (float): Manual entry for a start time, in epoch time.
            stop_time (float): Manual entry for an stop time, in epoch time.
        """
        # Backwards compatibility from python2 to python3
        # TODO. Find out if this is the appropriate place to put it?
        self.__nonzero__ = self.__bool__

        self._name = name
        self._start_time = start_time or time.time()
        self._stop_time = stop_time or None

    @property
    def name(self):
        """
        """
        return self._name

    @property
    def start_time(self):
        """ 
        """
        return time.ctime(self._start_time)

    @property
    def stop_time(self):
        """
        """
        if self._stop_time:
            return time.ctime(self._stop_time)

    def stop_process(self):
        """
        """
        self._stop_time = time.time()

    def __str__(self):
        """ Return a string description of the class.
        Returns:
            (str) description of the class.
        """
        return ("""
{
    %s: {
        start_time: %s,
        stop_time: %s
    }
}""" % (self._name, self._start_time, self._stop_time)
        )

    def __repr__(self):
        """ Return a string representation of the class.
        Returns:
            (str) representation of the class.
        """
        # Check required to be able to pass None or quote wraped string
        # into the repr.
        name = self._name
        if name:
            name = name.__repr__()

        return ("Process(%s, start_time=%s, stop_time=%s)" %
            (name, self._start_time, self._stop_time)
        )

    def __bool__(self):
        """ Value to return when for bool operation on a Process.
        Returns:
            (bool) True if the instance represents a valid process.
            False otherwise.
        """
        return True if self._name is not None else False
