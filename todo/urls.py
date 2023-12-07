from django.urls import path
from . import views

urlpatterns=[
  path('add/',views.addTask,name='addTask'),
  path('mark_as_done/<int:id>',views.mark_as_done,name='mark_as_done'),
  path('edit_task/<int:id>',views.edit_task,name='edit_task'),
  path('delete_task/<int:id>',views.delete_task,name='delete_task'),

]