import unittest, sys, os
from src.Utils.Shell import shell


def check_binary_access(cmd):
    stdo, stde, status = shell(cmd, verbose=True)
    return status == 0


class EnkiDevOpsUnitTest(unittest.TestCase):
    def setUp(self):
        os.environ['TEST_MODE'] = "True"

    @classmethod
    def setUpClass(cls):
        pass  # setup ce qui faut

    def test_001_SubDomainizer(self):
        self.assertTrue(check_binary_access(cmd='python3 SubDomainizer/SubDomainizer.py -h'))

    def test_002_Sublist3r(self):
        self.assertTrue(check_binary_access(cmd='python3 Sublist3r/sublist3r.py -h'))

    def test_003_subcat(self):
        self.assertTrue(check_binary_access(cmd='python3 subcat/subcat.py -h'))

    # def test_004_SecretFinder(self):
    #     cmd = ''
    #     self.assertTrue()
    #
    # def test_005_LinkFinder(self):
    #     cmd = ''
    #     self.assertTrue()

    def test_006_subfinder(self):
        self.assertTrue(check_binary_access(cmd='subfinder -h'))

    def test_007_gau(self):
        self.assertTrue(check_binary_access(cmd='gau -h'))

    def test_008_httpx(self):
        self.assertTrue(check_binary_access(cmd='httpx -h'))

    def test_009_assetfinder(self):
        self.assertTrue(check_binary_access(cmd='assetfinder -h'))

    def test_0010_gospider(self):
        self.assertTrue(check_binary_access(cmd='gospider -h'))

    def test_0011_waybackurls(self):
        self.assertTrue(check_binary_access(cmd='waybackurls -h'))

    def test_0012_jsubfinder(self):
        self.assertTrue(check_binary_access(cmd='jsubfinder -h'))

    def test_0012_hakrawler(self):
        self.assertTrue(check_binary_access(cmd='hakrawler -h'))

    @classmethod
    def tearDownClass(cls):
        pass  # clean ce qui faut


if __name__ == '__main__':
    sys.path.insert(0, os.getcwd())
    print(f'Tests bypass le temps que la C.I est construite sur les multi Dockers')
    # TODO: tests binary
    unittest.main(verbosity=2)
