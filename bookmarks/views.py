from django.shortcuts import render, redirect

from forms import AddGitHubAccountForm


def home(request):
    return render(request, 'bookmarks/home.html')


def github_connect(request):
    form = AddGitHubAccountForm()

    if request.method == 'POST':
        form = AddGitHubAccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()
            return redirect('home')
    return render(request, 'bookmarks/github_connect.html', {'form': form})


def github_sync(request):
    request.user.githubaccount.sync_repos()
    return redirect('home')
