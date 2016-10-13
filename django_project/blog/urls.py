from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^$', views.home, name='blog.home'),
    url(r'category/(?P<category_id>\d+)', views.show_posts_by_category, name='blog.posts_by_category'),
    url(r'^auth$', views.auth, name='blog.auth'),
    url(r'^logout$', views.logout_view, name='blog.logout'),
    url(r'^post_create', views.post_create, name='blog.post_create'),
]
