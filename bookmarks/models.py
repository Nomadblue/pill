from django.db import models
from django.contrib.auth import get_user_model
import requests
import json


class GitHubAccount(models.Model):
    user = models.OneToOneField(get_user_model())
    login = models.CharField(max_length=40)
    token = models.CharField(max_length=40)

    def _get_auth(self):
        return requests.auth.HTTPBasicAuth(self.login, self.token)

    def get_repos(self):
        r = requests.get('https://api.github.com/user/starred', auth=self._get_auth())
        if r.ok:
            return json.loads(r.text)
        else:
            return []

    def sync_repos(self):
        basic_fields = ['id', 'name', 'description', 'html_url']
        repos = self.get_repos()

        def create_repo(repo):
            extra_data = {field: repo[field] for field in [key for key in repo.keys() if key not in basic_fields]}
            basic_data = {field: repo[field] for field in basic_fields}
            return GitHubRepo.objects.get_or_create(github_account=self,
                                                    owner=repo['owner']['login'],
                                                    extra_data=json.dumps(extra_data),
                                                    **basic_data)

        return map(create_repo, repos)


class GitHubRepo(models.Model):
    github_account = models.ForeignKey(GitHubAccount)
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=40)
    description = models.TextField()
    html_url = models.CharField(max_length=200)
    extra_data = models.TextField()
