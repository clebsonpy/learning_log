""""Define padroes de URL para learning_logs."""
from django.conf.urls import url
from . import views

urlpatterns = [
    #Pagina Inicial
    url(r'^$', views.index, name='index'),

    #Mostra todos os assuntos
    url(r'^topics/$', views.topics, name='topics'),

    #Pagina de detalhes para um unico assunto
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    #Pagina para adicionar um novo assunto
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    #Pagina para adicionar uma nova entrada
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    #Pagina para editar uma entrada
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
