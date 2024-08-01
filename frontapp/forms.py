from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','cover_image','category','short_description', 'content', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'content': SummernoteWidget(),
            'short_description': SummernoteWidget(),
            #'category': forms.Select(attrs={'class': 'form-control w-100'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['content'].required = True
        self.fields['short_description'].required = True
        self.fields['status'].required = True
        self.fields['cover_image'].required = True


    def clean(self):
        # Custom validation logic here
        cleaned_data = super().clean()
        # Do not expect 'styles' or any other keyword arguments here
        # If 'styles' needs to be handled, it should be done elsewhere in the form logic
        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data['title']
        if Post.objects.filter(title=title).exists():
            if self.instance:
                if self.instance.title != title:
                    raise forms.ValidationError('Title must be unique')
            else:
                raise forms.ValidationError('Title must be unique')
        return title