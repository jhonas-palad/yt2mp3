from django import forms
from django.utils.regex_helper import _lazy_re_compile
from django.core.exceptions import ValidationError

YT_URL_REGEX = r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"

class YTUrlForm(forms.Form):
    yt_url = forms.URLField(
        widget= forms.TextInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['yt_url'].widget.attrs.update({
            'class': 'w-100',
            'autocomplete': 'off',
            'autocorrect': 'off',
            'placeholder':'Search or paste Youtube link here'
        })
        self.regex_compiled = _lazy_re_compile(YT_URL_REGEX)
    
    def clean_url(self):
        url = self.cleaned_data['url']
        regex_matches = self.regex_compiled.search(str(url))
        invalid_input = not regex_matches
        if invalid_input:
            raise ValidationError("Please enter a YouTube URL")
        return url
