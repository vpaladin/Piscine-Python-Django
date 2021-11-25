from django import forms
from .models import Movies

class OpenCrawl(forms.ModelForm):
    def __init__(self, round_list, *args, **kwargs):
        super(OpenCrawl, self).__init__(*args, **kwargs)
        self.fields["title"] = forms.CharField(widget=forms.Select(choices=tuple([(title, title) for title in round_list])))

    class Meta:
        model = Movies
        fields = ('title', "opening_crawl")


    


# class AddRatingForRound(forms.ModelForm):

#     def __init__(self, round_list, *args, **kwargs):
#         super(AddRatingForRound, self).__init__(*args, **kwargs)
#         self.fields['name'] = forms.ChoiceField(choices=tuple([(name, name) for name in round_list]))

#     class Meta:
#         model = models.RatingSheet
#         fields = ('name', )
