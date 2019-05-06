from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ Allows user to edit their own profile. """

    def has_object_permission(self, request, view, obj):
        """ Check user is trying to edit their own profile."""

        """ safe() is an HTTP method that is classified as safe i.e. its a non-destructive method because it doesnt allow you to change or delete any object in the system. """
        """ GET is a safe method. With GET user can view other user's profile but not edit. """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id

class PostOwnStatus(permissions.BasePermission):
        """ Allows users to update their own profile. """

        def has_object_permission(self, request, view, obj):
            """ Checks the user the user is trying to update their own status. """

            if request.method in permissions.SAFE_METHODS:
                return True

            return obj.id == request.user.id
