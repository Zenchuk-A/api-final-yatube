from rest_framework.permissions import IsAuthenticatedOrReadOnly, SAFE_METHODS


class IsReadOnlyOrAuthenticatedOrAuthor(IsAuthenticatedOrReadOnly):

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or obj.author == request.user
