import os
import logging

from psp.process import Process

_log = logging.getLogger('ProcessManager')

class ProcessManager(object):
    """ Manage the starting, stopping, recording, and reading of processes.

    Class Attributes:
        _current_process (Process): Keep track of what process is currently running.
    """

    def __init__(self, log_file, current_process_file):
        """
        """
        self._log_file = log_file
        self._current_process_file = current_process_file

        self._current_process = self._get_current_process_from_file()

    def start_process(self, name):
        """ Start a new process.
        Stops any current process.
        Write out the current process to the file.
        Args:
            name (str): Name of the process to start.
        """
        if self._current_process:
            self.stop_process()
        _log.debug('Starting process %s', name)
        self._current_process = Process(name)
        self._set_current_process_to_file()

    def stop_process(self):
        """ Stop the current process.
        Export the Process to the log.
        """
        _log.debug('Stoping current process %s', self._current_process.name)
        self._current_process.stop_process()
        self.export_process()
        self._current_process = None
        self._set_current_process_to_file()

    def export_process(self):
        """ Write out the current process to the file (or db).
        """
        _log.debug("Export process %s to %s",
            self._current_process.name,
            self._log_file,
        )
        exportFile = open(self._log_file, 'a')
        exportFile.write(str(self._current_process))
        exportFile.close()

    def _get_current_process_from_file(self):
        """ Read the current process from the current process file.
        Returns:
            (Process)
        """
        if not os.path.exists(self._current_process_file):
            return None
        _log.debug("Getting current process from %s",
            self._current_process_file
        )
        f = open(self._current_process_file, 'r')
        return eval(f.readline())

    def _set_current_process_to_file(self):
        """ Set a new process as the current process.
        Write out the new current process' repr to a file.
        """
        _log.debug("Writing current process %s to %s",
            self._current_process.name,
            self._current_process_file,
        )
        f = open(self._current_process_file, 'w')
        f.write(self._current_process.__repr__())
