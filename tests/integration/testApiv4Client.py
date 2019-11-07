'''
Created on Oct 23, 2019

@author: crackphantom
'''
import unittest
from tests.integration import settings
from ghvdc.clients import ApiV4


class Test(unittest.TestCase):


    def testGetVulnerableDependenciesForRepository(self):
        client = ApiV4(settings.TOKEN)
        response = client.getVulnerableDependenciesForRepository(settings.REPO_OWNER, settings.REPO_NAME)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()