import unittest, sys, os


class EnkiDevOpsUnitTest(unittest.TestCase):
    def setUp(self):
        os.environ['TEST_MODE'] = "True"

    @classmethod
    def setUpClass(cls):
        pass  # setup ce qui faut

    def test_001_SubDomainizer(self):
        cmd = 'python3 SubDomainizer/SubDomainizer.py -u'
        self.assertTrue()

    def test_002_Sublist3r(self):
        cmd = 'python3 Sublist3r/sublist3r.py  -h'
        self.assertTrue()

    def test_003_subcat(self):
        cmd = 'python3 subcat/subcat.py -silent'
        self.assertTrue()

    # def test_004_SecretFinder(self):
    #     cmd = ''
    #     self.assertTrue()
    #
    # def test_005_LinkFinder(self):
    #     cmd = ''
    #     self.assertTrue()

    def test_006_subfinder(self):
        cmd = 'subfinder -silent'
        self.assertTrue()

    def test_007_gau(self):
        cmd = 'gau -h'
        self.assertTrue()

    def test_008_httpx(self):
        cmd = 'httpx -h'
        self.assertTrue()

    def test_009_assetfinder(self):
        cmd = 'assetfinder -h'
        self.assertTrue()

    def test_0010_gospider(self):
        cmd = 'gospider -h'
        self.assertTrue()

    def test_0011_waybackurls(self):
        cmd = 'waybackurls -h'
        self.assertTrue()

    def test_0012_jsubfinder(self):
        cmd = 'jsubfinder -h'
        self.assertTrue()

    def test_0012_hakrawler(self):
        cmd = 'hakrawler -h'
        self.assertTrue()

    @classmethod
    def tearDownClass(cls):
        pass  # clean ce qui faut


if __name__ == '__main__':
    sys.path.insert(0, os.getcwd())
    print(f'Tests bypass le temps que la C.I est construite sur les multi Dockers')
    # TODO: tests binary
    unittest.main(verbosity=2)
