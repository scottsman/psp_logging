from argparse import ArgumentParser

class PspParser(object):
    """ Wrapper around ArgumentParser for psp specific arguments.
    """
    # Valid process name
    _valid_processes = {
        'code-review': ['cr', 'code'],
        'triage': ['tr'],
        'p2p': ['user', 'p2'],
    }

    # Valid action names
    _valid_actions = [
        'start',
        'stop',
    ]

    def __init__(self, args=None):
        """
        """
        self._parser = ArgumentParser()
        self._add_arguments()

    @property
    def parser(self):
        return self._parser

    def _add_arguments(self):
        """ Add psp specific arguments to the parser.
        """
        self._parser.add_argument('name', metavar='NAME',
            choices=self._valid_processes.keys(), nargs=1,
            help=(
                "Name of the process you are manipulating. "
                "Valid processes: %s." %
                [key for key in self._valid_processes.keys()]
            )
        )
        self._parser.add_argument('action', metavar='ACTION',
            choices=self._valid_actions, nargs=1,
            help=(
                "Action to apply to the process. "
                "Valid options: %s." % self._valid_actions
            )
        )
        self._parser.add_argument('-v', '--verbosity',
            action='count', default=0,
            help="Specify the level of verbosity."
        )

    def parse_args(self, args=None):
        """ Parse the arguments passed in or from `parse_args` default
        """
        return self._parser.parse_args(args=args)
