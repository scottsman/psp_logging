from psp import process

class ProcessManager(object):
    """ Manage the starting, stopping, recording, and reading of processes.
    """

    def __init__(self):
        """
        """
        pass

    def start_process(self, name):
        """ Start a new process.

        Args:
            name (str): Name of the process to start.
        """
        new_process = process.Process(name)

    def end_process(self):
        """ End the current process.
        """
        pass
