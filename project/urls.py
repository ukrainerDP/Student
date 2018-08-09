from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='index'),

	path('<int:question_id>/', views.general, name='general'),
	path('<int:question_id>/results', views.results, name='results'),
	path('<int:question_id>/detail', views.detail, name='detail')

] 

