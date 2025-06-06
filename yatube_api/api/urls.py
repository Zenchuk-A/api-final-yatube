from django.urls import path, include
from rest_framework import routers


from api.views import (
    PostViewSet,
    CommentViewSet,
    GroupViewSet,
    FollowViewSet,
)

router_v1 = routers.DefaultRouter()
router_v1.register('posts', PostViewSet)
router_v1.register(
    'posts/(?P<post_id>[0-9]+)/comments',
    CommentViewSet,
    basename='post-comments',
)
router_v1.register('groups', GroupViewSet)
router_v1.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
