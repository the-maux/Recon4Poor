import os
from src.Utils.Shell import VERBOSE


def sanity_check_at_startup():
    """
        [X] Check if target is alive
        [X] Check if all binary are present & configured
        [X] Check if all variable are present (TODO: Dynamic conf regarding the env var present)
    """
    try:
        depth = int(os.environ['DEPTH'])
        if VERBOSE:
            print(f'(DEBUG) DEPTH analyse was not set, default is {os.environ["DEPTH"]}')
    except Exception:
        if VERBOSE:
            print('(WARNING) DEPTH analyse was not set, default is 1')
        depth = 1
    try:
        target = os.environ['TARGET']
        return target, depth
    except Exception as e:
        print(f'(ERROR) You need to set at least the var env $TARGET: {e}')
        exit(-1)
