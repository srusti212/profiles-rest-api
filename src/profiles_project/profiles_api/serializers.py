from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    """ Serializes a name field for testing our APIView. """
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
        """ Serializes our user profile object. """

        class Meta:
            model = models.UserProfile
            fields = ['id', 'name', 'email', 'password']
            # Special attributes we wish to apply to fileds
            extra_kwargs = {'password': {'write_only':True}}

        # Overriding default functionality
        def create(self, validated_data):
            """ Create and return a new user. """

            user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
            )
            """ Encrypting password as a hash instead of storing the clear text password in the database """
            user.set_password(validated_data['password'])
            user.save()
            return user
