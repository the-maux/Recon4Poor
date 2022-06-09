import unittest, sys, os


class EnkiDevOpsUnitTest(unittest.TestCase):
    def setUp(self):
        os.environ['TEST_MODE'] = "True"

    @classmethod
    def setUpClass(cls):
        pass  # setup ce qui faut

    def test_001_SubDomainizer(self):
        self.assertTrue()

    def test_002_Sublist3r(self):
        self.assertTrue()

    def test_003_subcat(self):
        self.assertTrue()

    def test_004_SecretFinder(self):
        self.assertTrue()

    def test_005_LinkFinder(self):
        self.assertTrue()

    def test_006_subfinder(self):
        self.assertTrue()

    def test_007_gau(self):
        self.assertTrue()

    def test_008_httpx(self):
        self.assertTrue()

    def test_009_assetfinder(self):
        self.assertTrue()

    def test_0010_gospider(self):
        self.assertTrue()

    def test_0011_waybackurls(self):
        self.assertTrue()

    def test_0012_jsubfinder(self):
        self.assertTrue()

    def test_0012_hakrawler(self):
        self.assertTrue()


    @classmethod
    def tearDownClass(cls):
        pass  # clean ce qui faut


if __name__ == '__main__':
    sys.path.insert(0, os.getcwd())
    print(f'Tests bypass le temps que la C.I est construite sur les multi Dockers')
    # TODO: tests binary
    unittest.main(verbosity=2)
