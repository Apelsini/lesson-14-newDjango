from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('polls/', view=views.index, name='index'),
    path('details/<int:question_id>/', view=views.detail, name='detail'),
    path('polls/<int:question_id>/results/', view=views.results_view, name='results'),
    path('polls/<int:choice_id>/vote/', view=views.vote, name='vote'),
]