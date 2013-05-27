from argparse import ArgumentParser

class PspParser(object):
    """ Wrapper around ArgumentParser for psp specific arguments.
    """
    # Valid process name
    _valid_processes = {
        'bug-fixing': ['b', 'bf', 'bug', 'bug-fixing'],
        'code-review': ['c', 'cr', 'code', 'code-review'],
        'development': ['d', 'dev', 'development'],
        'investigating': ['i', 'inv', 'investigating'],
        'p2p': ['p', 'user', 'p2p',],
        'triage': ['t', 'tr', 'triage'],
    }

    # Valid action names
    _valid_actions = {
        'begin': ['b', 'begin'],
        'end': ['e', 'end'],
    }

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
        valid_processes = []
        for valid_process_names in self._valid_processes.values():
            valid_processes.extend(valid_process_names)
        self._parser.add_argument('name', metavar='NAME',
            choices=valid_processes, nargs=1,
            help=(
                "Name of the process you are manipulating. "
                "Valid processes: %s." % self._valid_processes
            )
        )
        valid_actions = []
        for valid_action_names in self._valid_actions.values():
            valid_actions.extend(valid_action_names)
        self._parser.add_argument('action', metavar='ACTION',
            choices=valid_actions, nargs=1,
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

    def get_process_name(self, abbreviation):
        """ Get the process name from the abbreviation.
        eg:
            If the user enters 'bug', then 'bug-fixing' will be returned.
        Returns:
            (str) Name of the process the abbreviation is short for.
            None if process name is not found.
        """
        for valid_process_name, valid_process_abbreviations in self._valid_processes.items():
            if abbreviation in valid_process_abbreviations:
                return valid_process_name
        return None

    def get_action_name(self, abbreviation):
        """ Get the action name from the abbreviation.
        eg:
            If the user enters 'b', then 'begin' will be returned.
        Returns:
            (str) Name of the action the abbreviation is short for.
            None if action name is not found.
        """
        for valid_action_name, valid_action_abbreviations in self._valid_actions.items():
            if abbreviation in valid_action_abbreviations:
                return valid_action_name
        return None
