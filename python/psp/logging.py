import logging

def setup(verbosity_level=0):
    """ Set up logging for the project.
    TODO. Implement a more elegant solution, if needed.
    Args:
        verbosity_level (int): level of verbosity. A higher number
            means more verbose. Max = 3. Default = 0.
    """
    # Sort out logging level.
    default_level = logging.ERROR # 40
    new_level = default_level - (verbosity_level * 10)

    # Set up base logger and handler.
    _log = logging.getLogger()
    _handler = logging.StreamHandler()
    _log.setLevel(new_level)
    _handler.setLevel(new_level)
    _log.addHandler(_handler)
