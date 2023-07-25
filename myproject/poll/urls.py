from django.urls import path

from . import views


app_name="poll"
urlpatterns = [
    path("__debug__/",include("dabug_toolbar.urls")),
    path("", views.indexView.as_view(), name="index"),
    path("<int:pk>/",views.DetailView.as_view(),name="detail"),
    path("<int:pk>/results",views.ResultsView.as_view(),name="results"),
    path("<int:question_id>/vote",views.vote,name="vote"),
]