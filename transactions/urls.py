from django.urls import path

from . import views

urlpatterns = [
    # ex: /transactions/
    path('', views.index, name='index'),
    # ex: /transactions/pending
    path('pending/', views.pending, name='pending'),
    # ex: /transactions/create/
    path('create/', views.create, name='create'),
    # ex: /transactions/mine/
    path('mine/', views.mine, name='mine'),
]
