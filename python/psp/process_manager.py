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
        """ ProcessManager initialization.
        Args:
            log_file (str): Path to log file. Used for exporting each new
                psp process to.
            current_process_file (str): Path to process file. Used to store
                the current process.
        """
        self._log_file = log_file
        self._current_process_file = current_process_file

        self._current_process = self._get_current_process_from_file()

        _log.debug(self.__str__())

    def __str__(self):
        """ Return a string summary of the current ProcessManager.
        Returns:
            (str) ProcessManager summary.
        """
        return (
            "ProcessManager: Log file is: %s. Process file is %s. "
            "Current process is %s" % (
                self._log_file,
                self._current_process_file,
                self._current_process.name
            )
        )

    def __repr__(self):
        """ Return a representation of the current ProcessManager.
        Returns:
            (str) ProcessManager representation.
        """
        return ("ProcessManager(%s, %s)" %
            (self._log_file, self._current_process_file)
        )
    def start_process(self, name):
        """ Start a new process.
        Stops any current process.
        Write out the current process to the file.
        Args:
            name (str): Name of the process to start.
        """
        _log.info('Starting current process.')
        if self._current_process:
            _log.info('Stopping previous current process first')
            self.stop_process()
        _log.debug('Starting process %s', name)
        self._current_process = Process(name)
        self._set_current_process_to_file()
        _log.info('Done starting current process.')

    def stop_process(self):
        """ Stop the current process.
        Export the Process to the log.
        """
        _log.info("Stopping current process")
        if not self._current_process:
            _log.debug('No current process to stop')
            return
        _log.debug('Stoping current process %s', self._current_process.name)
        self._current_process.stop_process()
        self._export_process()
        self._current_process = Process(None)
        self._set_current_process_to_file()
        _log.info("Stopped current process")

    def _export_process(self):
        """ Write out the current process to the file (or db).
        """
        _log.info("Exporting current process")
        _log.debug("Export process %s to %s",
            self._current_process.name,
            self._log_file,
        )
        exportFile = open(self._log_file, 'a')
        exportFile.write(str(self._current_process))
        exportFile.close()
        _log.info("Done exporting current process")

    def _get_current_process_from_file(self):
        """ Read the current process from the current process file.
        Returns:
            (Process)
        """
        _log.info('Getting current process.')
        if not os.path.exists(self._current_process_file):
            _log.info('No current process exists.')
            return Process(None)
        _log.debug("Getting current process from %s",
            self._current_process_file
        )
        f = open(self._current_process_file, 'r')
        current_process = f.readline() or Process(None)
        _log.info('Done getting current process.')
        return eval(current_process)

    def _set_current_process_to_file(self):
        """ Set a new process as the current process.
        Write out the new current process' repr to a file.
        Note:
            At this point _current_process can be None.
        """
        _log.info('Writing current process.')
        name = None
        repr = 'None'
        if self._current_process:
            name = self._current_process.name
            repr = self._current_process.__repr__()
        _log.debug("Writing current process %s to %s",
            name,
            self._current_process_file,
        )
        f = open(self._current_process_file, 'w')
        f.write(repr)
        _log.info('Done writing current process.')
