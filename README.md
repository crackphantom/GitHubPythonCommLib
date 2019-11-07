# GitHubVulnerableDependenciesClient

Collection of queries to GitHub v4 (GraphQL) API to programmatically collect vulnerabilities in GitHub repositories

## The Vulnerable Dependencies feature in GitHub

### About

### Notifications

### Enabling
blurb about the setting in the repo

your user needs the ability to view vulnerabilities for a repo which is the owner role

## What each method returns
getVulnerableDependenciesForRepository - Given an owner (org/name) and repo, get all the open vulnerabilities

## Authentication

### Personal access tokens

The code was developed and tested with personal access tokens.
To generate your own GitHub personal access token, use the following resources

https://developer.github.com/v4/guides/forming-calls/#authenticating-with-graphql
https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line

### Troubleshooting OAuth scopes

The response {"data":{"repository":null}} is an indication of the token having insufficient rights.

Run the following to check to see what OAuth scopes the token you are using has, and what the API action (graphql) accepts

curl -H "Authorization: token OAUTH-TOKEN" https://api.github.com/graphql -I

X-OAuth-Scopes lists the scopes your token has authorized.
X-Accepted-OAuth-Scopes lists the scopes that the action checks for.



Further details
https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/