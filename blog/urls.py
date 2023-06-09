from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('review_page/', views.ReviewPage.as_view(), name='review_page'),
    path('review/new/', views.ReviewCreate.as_view(), name='review_create'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('<slug:slug>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]