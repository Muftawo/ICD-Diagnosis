from django.urls import path
from .views import CodeList,CodeDetail,CategoryList,CategoryDetail

urlpatterns = [
    path('codes/', CodeList.as_view()),
    path('code/<int:pk>',CodeDetail.as_view()),
    path('category/', CategoryList.as_view()),
    path('category/<int:pk>',CategoryDetail.as_view())
]
