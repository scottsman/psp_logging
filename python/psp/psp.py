import psp.logging
from psp.process_manager import ProcessManager
from psp.argument_parser import PspParser

def main():
    """ Main function for controlling psp processes.
    """
    # Parse args.
    parser = PspParser()
    args = parser.parse_args()

    # Set up internal logging.
    psp.logging.setup(verbosity_level=args.verbosity)

    # Create a ProcessManager.
    _log_file = '/tmp/psp.log'
    _current_process_file = '/tmp/current_process'
    manager = ProcessManager(
        _log_file,
        _current_process_file
    )

    # Run actions on processes using the ProcessManager.
    action_name = parser.get_action_name(args.action[0])
    process_name = parser.get_process_name(args.name[0])
    if action_name == 'begin':
        manager.start_process(process_name)
    elif action_name == 'end':
        manager.stop_process()
