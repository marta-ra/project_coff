from django.urls import reverse, reverse_lazy

from .models import Visit
from .models import Useful_code
from .models import Useful_docs
from django.forms import ModelForm


class VisitForm(ModelForm):
    class Meta:
        model = Visit
        fields = ['coffemachine', 'visit_date', 'technical_specialist', 'done', 'renovation', 'what_renovation']

class Useful_codeForm(ModelForm):
    class Meta:
        model = Useful_code
        fields = ['description', 'code']

class Useful_docsForm(ModelForm):
    class Meta:
        model = Useful_docs
        fields = ['model_machine', 'document']

        # success_url = reverse_lazy('create_useful_docs')