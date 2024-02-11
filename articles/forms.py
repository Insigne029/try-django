from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
            model = Article
            fields = ["title","content"]
            
            
    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error("title", "This title has already been taken")
        return data
        


# class ArticleFormOld(forms.Form):
#     titile = forms.CharField()
#     content = forms.CharField()
    
    
#     def clean_title(self):
#         cleaned_data = self.cleaned_data
#         title = cleaned_data.get("title")
#         print(f"Cleaned title: {title}")
#         if title.lower().strip() == "the office":
#             raise forms.ValidationError("This title is already taken")

#         return title


#     def clean(self):
#         cleaned_data = self.cleaned_data
#         print(f"All cleaned data: {cleaned_data}")
        
#         return cleaned_data