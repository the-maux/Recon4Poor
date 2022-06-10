import unittest, sys, os
from src.Utils.Shell import shell
from src.main import B4DID34T

def check_binary_access(cmd):
    stdo, stde, status = shell(cmd, verbose=True)
    return status == 0 or status == 2  # 3 for hakrawler


class EnkiDevOpsUnitTest(unittest.TestCase):
    def setUp(self):
        os.environ['TEST_MODE'] = "True"

    @classmethod
    def setUpClass(cls):
        pass  # setup ce qui faut

    def test_001_dependencys(self):
        self.assertTrue(check_binary_access(cmd='python3 SubDomainizer/SubDomainizer.py -h'))
        self.assertTrue(check_binary_access(cmd='python3 Sublist3r/sublist3r.py -h'))
        self.assertTrue(check_binary_access(cmd='python3 subcat/subcat.py -h'))
        self.assertTrue(check_binary_access(cmd='subfinder -h'))
        self.assertTrue(check_binary_access(cmd='gau -h'))
        self.assertTrue(check_binary_access(cmd='httpx -h'))
        self.assertTrue(check_binary_access(cmd='assetfinder -h'))
        self.assertTrue(check_binary_access(cmd='waybackurls -h'))
        self.assertTrue(check_binary_access(cmd='jsubfinder -h'))
        self.assertTrue(check_binary_access(cmd='hakrawler -h'))

    def test_002_basic_scan(self):
        B4DID34T(domains=os.environ['TARGET'])


    # def test_004_SecretFinder(self):
    #     cmd = ''
    #     self.assertTrue()
    #
    # def test_005_LinkFinder(self):
    #     cmd = ''
    #     self.assertTrue()

    # def test_0010_gospider(self):
    #     self.assertTrue(check_binary_access(cmd='gospider -h'))

    @classmethod
    def tearDownClass(cls):
        pass  # clean ce qui faut


if __name__ == '__main__':
    sys.path.insert(0, os.getcwd())
    print(f'Tests bypass le temps que la C.I est construite sur les multi Dockers')
    # TODO: tests binary
    unittest.main(verbosity=2)
