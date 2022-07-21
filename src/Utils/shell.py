import subprocess, os

try:
    VERBOSE = 'True' in os.environ['VERBOSE']
except Exception:
    VERBOSE = True


def dump_to_file(namefile, lines, mode='w', filterdomain=True):
    """ Dump a file, possibility to filter only on domain """
    end_domain = ['.eu', '.fr', '.com', '.ru', '.rui', '.pl', '.org']
    with open(namefile, mode) as f:
        for line in lines:
            if filterdomain is False or (filterdomain and any([word in line for word in end_domain])):
                f.write(f"{line}\n")


def filter_bullshitshell(logs, bypassed_words=None):
    """
        filtering the shell logs that is useless
        :options list de substrings a remove (bypassed_words)
        :return logs in one string, with \n
    """
    logs = logs.decode('utf-8', errors='replace').strip()
    if bypassed_words is None:
        bypassed_words = ['setlocale: LC_CTYPE: cannot change locale', 'Warning: Permanently added']
    return '\n'.join([log for log in logs.split('\n') if not any([word in log for word in bypassed_words])])


def shell(cmd, verbose=None, outputOnly=None):
    """
        Exec shell cmd & filter outputs
        :return: stdout, stderror, & exit_status
    """
    if (verbose is not None and verbose is True) or (verbose is None and VERBOSE):
        print(f'$> {cmd}')
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, executable='/bin/bash')
    (stdout, stderr) = p.communicate()
    p.wait()
    stdout = filter_bullshitshell(stdout)
    stderr = filter_bullshitshell(stderr)
    return stdout if outputOnly is True else (stdout, stderr, p.returncode)

name: 3- Start Scan on target

on: push

jobs:
  Scanning:
#    if: startsWith(github.event.head_commit.message, 'SCAN')
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
    container:
      image: ghcr.io/the-maux/recoon4poor:latest
      #      options: -v ${{ github.workspace }}:/opt/recoon
      credentials:
        username: ${{ github.actor }}
        password: ${{ secrets.GHCR_TOKEN }}
    env:
      GITHUB_PASSWD: ${{ secrets.GITHUB_TOKEN }}
      USER_EMAIL: ${{ secrets.USER_EMAIL }}
      USER_PASSWORD: ${{ secrets.USER_EMAIL_PASSWORD }}
      TARGET: ${{ secrets.TARGET }}
      DEPTH: ${{ secrets.DEPTH }}
    - name: Start the scan from docker image
      run: |
        ls
        python src/main.py
