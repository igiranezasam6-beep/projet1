from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Exercise, ExerciseComment, ForumPost, ForumTopic, Profile


class StudentSignUpForm(UserCreationForm):
    email = forms.EmailField(required=False)
    school_level = forms.CharField(
        required=True,
        max_length=50,
        help_text="Ex: 7e, 8e, 9e, 1re, 2e, 3e, Terminale…",
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "school_level", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if not isinstance(field.widget, (forms.CheckboxInput, forms.RadioSelect)):
                field.widget.attrs.setdefault("class", "form-control")

    def save(self, commit: bool = True):
        user = super().save(commit=commit)
        profile, _ = Profile.objects.get_or_create(user=user)
        profile.role = Profile.Role.STUDENT
        profile.is_verified = True
        profile.school_level = self.cleaned_data["school_level"]
        if commit:
            profile.save()
        return user


class TeacherSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    school_level = forms.CharField(
        required=False,
        max_length=50,
        help_text="Niveau principal (optionnel). Ex: Lycée, Collège, 9e…",
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "school_level", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if not isinstance(field.widget, (forms.CheckboxInput, forms.RadioSelect)):
                field.widget.attrs.setdefault("class", "form-control")

    def save(self, commit: bool = True):
        user = super().save(commit=commit)
        profile, _ = Profile.objects.get_or_create(user=user)
        profile.role = Profile.Role.TEACHER
        profile.is_verified = False  # validation via admin
        profile.school_level = self.cleaned_data.get("school_level", "")
        if commit:
            profile.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = (
            "subject",
            "school_level",
            "theme",
            "title",
            "description",
            "exercise_file",
            "correction_file",
            "correction_text",
            "video_url",
        )

        widgets = {
            "subject": forms.TextInput(attrs={"class": "form-control"}),
            "school_level": forms.TextInput(attrs={"class": "form-control"}),
            "theme": forms.TextInput(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "correction_text": forms.Textarea(attrs={"class": "form-control", "rows": 6}),
            "video_url": forms.URLInput(attrs={"class": "form-control"}),
        }


class ExerciseCommentForm(forms.ModelForm):
    class Meta:
        model = ExerciseComment
        fields = ("content",)
        widgets = {"content": forms.Textarea(attrs={"class": "form-control", "rows": 3})}


class ForumTopicForm(forms.ModelForm):
    class Meta:
        model = ForumTopic
        fields = ("subject", "school_level", "title")
        widgets = {
            "subject": forms.TextInput(attrs={"class": "form-control"}),
            "school_level": forms.TextInput(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
        }


class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ("content",)
        widgets = {"content": forms.Textarea(attrs={"class": "form-control", "rows": 4})}


class ChatbotForm(forms.Form):
    school_level = forms.CharField(required=False, max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    question = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Posez votre question…"}),
    )

