from django.urls import path

from . import views


urlpatterns = [
    path('new/', views.CreatePost.as_view(), name='post_new'),
    path('data/', views.DataView.as_view(), name='data_post'),
    path('pyjava/', views.PyJavaView.as_view(), name='pyjava_post'),
    path('ios/', views.iOSView.as_view(), name='ios_post'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<slug:slug>/edit/', views.PostUpdateView.as_view(), name='edit_post'),
    path('<slug:slug>/delete/', views.DeletePostView.as_view(), name='delete_post'),
]
