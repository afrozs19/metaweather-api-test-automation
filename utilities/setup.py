import os


def get_root_test_dir():
    """
        Returns the root directory of Testing Framework.
        This is to avoid any interruptions in the tests run.
    """
    root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    return root_dir
