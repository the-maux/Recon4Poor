import subprocess, os

try: VERBOSE = 'True' in os.environ['VERBOSE']
except Exception: VERBOSE = True


def filter_bullshitssh(logs, bypassed_words=None):
    """
        filtrer dans une list de logs, des substrings pour supprimer la ligne
        :options list de substrings a remove (bypassed_words)
        :return logs en string, séparé par des \n
    """
    logs = logs.decode('utf-8', errors='replace').strip()
    if bypassed_words is None:
        bypassed_words = ['setlocale: LC_CTYPE: cannot change locale',
                          'Warning: Permanently added']
    return ''.join([log for log in logs.split('\n') if not any([word in log for word in bypassed_words])])


def shell(cmd):
    """
        Exec shell cmd & filter outputs
        :return: stdout, stderror, & exit_status
    """
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, executable='/bin/bash')
    (stdout, stderr) = p.communicate()
    p.wait()
    stdout = filter_bullshitssh(stdout)
    stderr = filter_bullshitssh(stderr)
    return stdout, stderr, p.returncode
