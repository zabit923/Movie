from django import template
from django.apps import apps
from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField




class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = apps.get_model('contact', 'Contact')
        fields = ('email', 'captcha', )
        widgets = {
            'email': forms.TextInput(attrs={'class': 'editContent', 'placeholder': 'Enter your email...'})
        }
        labels = {
            'email': ''
        }


register = template.Library()


@register.inclusion_tag('contact/tags/form.html')
def contact_form():
    return {'contact_form': ContactForm()}