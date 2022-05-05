import os
from src.Scans.quick import quick_scan
from src.Scans.regular import regular_scan
from src.Scans.hard import hard_scan
from src.Analyze.send_report import sendMail


def analyse_scan(results):
    results = list()
    sendMail(results)
    return results


def fackMeButSmilePlz(target, depth):

    if depth == 1:
        results = quick_scan(target)
    elif depth == 2:
        results = regular_scan(target)
    else:
        results = hard_scan(target)
    return analyse_scan(results)


if __name__ == "__main__":
    # TODO: install check, if not present, start it
    try:
        fackMeButSmilePlz(os.environ['TARGET'], os.environ['DEPTH'])
    except Exception:
        print(f'You need to set the var $TARGET & $DEPTH to run it :)')