'''
Created on Oct 23, 2019

@author: crackphantom
'''
import unittest
from tests.integration import settings
from datadorks.pcomm.github.httpclients import ApiV4


class Test(unittest.TestCase):


    def testGetVulnerableDependenciesForRepository(self):
        client = ApiV4(settings.TOKEN)
        response = client.getVulnerableDependenciesForRepository(settings.REPO_OWNER, settings.REPO_NAME)
        self.assertIsNotNone(response)
        self.assertTrue(0 < len(response.get("data", {}).get("repository", {}).get("vulnerabilityAlerts", {}).get("nodes", [])))


if __name__ == "__main__":
    # Assuming you set PYTHONPATH to contain dependency e.g. 
    # export PYTHONPATH=/some/path/to/project/GenericPythonCommLib
    # /usr/bin/python2.7 -m unittest -v tests.integration.testApiv4Client.Test
    # /usr/bin/python3 -m unittest -v tests.integration.testApiv4Client.Test
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
