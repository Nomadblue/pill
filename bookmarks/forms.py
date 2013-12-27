from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button, Layout, Field
from crispy_forms.bootstrap import FormActions, AppendedText

from models import GitHubAccount


class AddGitHubAccountForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddGitHubAccountForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(FormActions(Submit('submit', 'Add')))

    class Meta:
        model = GitHubAccount
        exclude = ('user',)
