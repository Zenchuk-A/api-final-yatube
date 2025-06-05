from django.urls import path, include
from rest_framework import routers

from api.views import (
    PostViewSet,
    CommentViewSet,
    GroupViewSet,
    FollowViewSet,
)

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register(
    'posts/(?P<post_id>[0-9]+)/comments',
    CommentViewSet,
    basename='post-comments',
)
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
