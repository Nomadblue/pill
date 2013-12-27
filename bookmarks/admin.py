from django.contrib import admin

from models import GitHubAccount, GitHubRepo


class GitHubAccountAdmin(admin.ModelAdmin):
    pass


class GitHubRepoAdmin(admin.ModelAdmin):
    list_display = ('id', 'github_account', 'name', 'owner', 'description', 'html_url', 'description')


admin.site.register(GitHubAccount, GitHubAccountAdmin)
admin.site.register(GitHubRepo, GitHubRepoAdmin)
