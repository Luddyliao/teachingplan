from django.urls import path
from .views import TeachingplanList, TeachingplanCreate, TeachingplanUpdate, TeachingplanDelete, TeachingplanSemester, TeachingplanSemesterClass

urlpatterns = [
    path('', TeachingplanList.as_view(), name='teachingplan_list'), 
    path('create/', TeachingplanCreate.as_view(), name='teachingplan_create'),
    path('<int:pk>/delete/', TeachingplanDelete.as_view(), name='teachingplan_delete'),
    path('seme/<slug:seme>/', TeachingplanSemester.as_view(), name='teachingplan_semester'),
]
