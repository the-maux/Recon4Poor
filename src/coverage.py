import subprocess
from src.Utils.Shell import shell


if __name__ == '__main__':
    shell('/home/app/.local/bin/coverage run --source="." --rcfile=.coverage -m unittest src/unit_test.py')
    stdout, stderr, returncode = shell('/home/app/.local/bin/coverage report')
    print(stdout)
    try:
        pourcentage = int(stdout.split('\n')[-2].strip().split(' ')[-1].replace("%", ""))
    except ValueError as e:
        pourcentage = -1
        print(f'(ERROR) In coverage, cant analyse result {e}')
    if pourcentage < 40:
        print(f"(DEBUG) Pourcentage de coverage actuel [{pourcentage}]en dessous de 40% ><' !!! ")
        exit(-1)
    print('(DEBUG) Coverage checking OK !')
    exit(0)
