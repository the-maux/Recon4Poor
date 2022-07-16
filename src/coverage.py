import subprocess


def shell(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (stdout, stderr) = p.communicate()
    p.wait()
    return stdout.decode('utf-8',  errors='replace'), stderr.decode('utf-8',  errors='replace'), p.returncode


if __name__ == '__main__':
    shell("coverage run --rcfile=.coverage -m unittest src/unit_test.py")
    stdout, stderr, returncode = shell('coverage report')
    try:
        pourcentage = int(stdout.split('\n')[-2].strip().split(' ')[-1].replace("%", ""))
    except Exception as e:
        pourcentage = -1
        print(f'(ERROR) In coverage, cant analyse result {e}')
    if pourcentage > 40:
        print('(DEBUG) Coverage checking OK !')
        exit(0)
    else:
        print(f"(DEBUG) Pourcentage de coverage actuel [{pourcentage}]en dessous de 40% ><' !!! ")
    exit(-1)