import unittest, sys, os
from src.Utils.shell import shell
from src.main import B4DID34


def check_binary_access(cmd):
    stdo, stde, status = shell(cmd, verbose=False)
    return status == 0 or status == 2  # 3 for hakrawler


class UnitTests(unittest.TestCase):
    def setUp(self):
        os.environ['TEST_MODE'] = 'False'

    @classmethod
    def setUpClass(cls):
        pass  # setup ce qui faut

    def test_001_dependencys(self):
        self.assertTrue(check_binary_access(cmd='python SubDomainizer/SubDomainizer.py -h'))
        self.assertTrue(check_binary_access(cmd='python Sublist3r/sublist3r.py -h'))
        self.assertTrue(check_binary_access(cmd='python subcat/subcat.py -h'))
        self.assertTrue(check_binary_access(cmd='subfinder -h'))
        self.assertTrue(check_binary_access(cmd='gau -h'))
        self.assertTrue(check_binary_access(cmd='nuclei -h'))
        self.assertTrue(check_binary_access(cmd='httpx -h'))
        self.assertTrue(check_binary_access(cmd='assetfinder -h'))
        self.assertTrue(check_binary_access(cmd='waybackurls -h'))
        self.assertTrue(check_binary_access(cmd='jsubfinder -h'))
        self.assertTrue(check_binary_access(cmd='hakrawler -h'))
        self.assertTrue(check_binary_access(cmd='gospider -h'))
        self.assertTrue(check_binary_access(cmd='subjs -h'))
        self.assertTrue(check_binary_access(cmd='amass -h'))
        self.assertTrue(check_binary_access(cmd='gobuster -h'))
        self.assertTrue(check_binary_access(cmd='shuffledns -h'))
        self.assertTrue(check_binary_access(cmd='dmut -h'))
        self.assertTrue(check_binary_access(cmd='dnsx -h'))
#        self.assertTrue(check_binary_access(cmd='dnscan -h'))
#        self.assertTrue(check_binary_access(cmd='puredns -h'))

        # TOTEST
        # https://github.com/OWASP/Amass
        # https://github.com/projectdiscovery/dnsx a use ?
        # https://github.com/projectdiscovery/shuffledns
        # https://github.com/d3mondev/puredns
        # https://github.com/bp0lr/dmut moe
        # https://github.com/OJ/gobuster
        ### https://github.com/codingo/DNSCewl + https://github.com/ProjectAnte/dnsgen ??????
        # https://github.com/rbsec/dnscan python

    @classmethod
    def tearDownClass(cls):
        pass  # clean ce qui faut


def coverage_me():
    conf = """ 
[run]
omit =
    src/unit_test.py
[report]
exclude_lines =
    pragma: no cover
    if __name__ == .__main__.:
"""
    shell(cmd=f'echo -n {conf} > .coverage')
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


if __name__ == '__main__':
    if 'True' in os.environ['COVERAGE']:
        coverage_me()
    else:
        unittest.main(verbosity=2)
