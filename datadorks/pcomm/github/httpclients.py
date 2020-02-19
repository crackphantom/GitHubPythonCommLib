'''
Created on Oct 23, 2019

@author: crackphantom
'''

import json
from datadorks.pcomm.http.clients import factory

GITHUBV4_URL = 'https://api.github.com/graphql'
PAGE_SIZE = 10


class ApiV4(object):
    '''
    classdocs
    '''
    proxyclient = None


    def __init__(self, bearertoken):
        '''
        Constructor
        '''
        self.proxyclient = factory.getNewSyncHttpClient()
        self.bearertoken = bearertoken # personal access token
        
    def connect(self):
        pass

    def disconnect(self):
        pass
    
    def _checkResponse(self):
        # TODO handle bad responses like
        # {"data":{"repository":null},"errors":[{"type":"FORBIDDEN","path":["repository"],"locations":[{"line":1,"column":8}],"message":"Resource pro
        pass

    def getVulnerableDependenciesForRepository(self, repoOwner, repoName):
        nextPage = True
        nodes = []
        result = {"data":{"repository":{"name":repoName,"vulnerabilityAlerts":{"nodes":nodes}}}}
        queryString = "query {repository(owner:\"" + repoOwner + "\", name:\"" + repoName + "\") {name vulnerabilityAlerts(first:"+str(PAGE_SIZE)+") { edges { cursor } nodes { id vulnerableManifestFilename vulnerableManifestPath vulnerableRequirements securityVulnerability { advisory {databaseId description origin publishedAt summary} package { name ecosystem} severity vulnerableVersionRange } } pageInfo {endCursor hasNextPage} } } }"
        data = {"query": queryString}
        headers = {'Accept': 'application/vnd.github.vixen-preview+json',
                   'Authorization': 'bearer {}'.format(self.bearertoken)}
        
        while nextPage:
            nextPage = False
            response = self.proxyclient.doRequest('POST', GITHUBV4_URL, headers, json.dumps(data))
            if response.exists:
                try:
                    parsedResp = json.loads(response.body)
                    #if we have any nodes in this response, add to result
                    vAlerts = parsedResp.get('data', {}).get('repository', {}).get('vulnerabilityAlerts', {})
                    nodes.extend(vAlerts.get('nodes', []))
                    # do we have to do further pagination? do so if so
                    pageInfo = vAlerts.get('pageInfo', {})
                    if pageInfo.get('hasNextPage', False) and pageInfo.get('endCursor'):
                        nextPage = True
                        # call again, after 'endCursor' 
                        pageQueryString = "query {repository(owner:\"" + repoOwner + "\", name:\"" + repoName + "\") {name vulnerabilityAlerts(first:" + str(PAGE_SIZE) + " after:\"" + pageInfo.get('endCursor') + "\") { edges { cursor } nodes { id vulnerableManifestFilename vulnerableManifestPath vulnerableRequirements securityVulnerability { advisory {databaseId description origin publishedAt summary} package { name ecosystem} severity vulnerableVersionRange } } pageInfo {endCursor hasNextPage} } } }"
                        data = {"query": pageQueryString}
                except(KeyError, ValueError):
                    pass
            else:
                pass
        return result
    
    def getVulnerableDependenciesForOrganization(self):
        pass
    