from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note
import re


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        # extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user

    def validate_username(self, valuename):
        username_length = len(valuename)
        if username_length <= 5 or username_length >= 15:
            raise serializers.ValidationError(
                "Username must be greator than 5 and less than 15"
            )
        return valuename

    def validate_password(self, value):
        min_length = 8
        regex = (
            r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*()_+]).{"
            + str(min_length)
            + r",20}$"
        )

        if len(value) < min_length:
            raise serializers.ValidationError(
                f"Password must be at least {min_length} characters long."
            )

        if not re.fullmatch(regex, value):
            raise serializers.ValidationError(
                "Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character (!@#$%^&*()_+)."
            )
        return value

    # Regex for a strong password:
    # (?=.*[A-Z])  : Lookahead for at least one uppercase letter.
    # (?=.*[a-z])  : Lookahead for at least one lowercase letter.
    # (?=.*[0-9])  : Lookahead for at least one digit.
    # (?=.*[!@#$%^&*()_+]) : Lookahead for at least one symbol.
    # .{8,}        : Match any character at least 8 times.

    # validation of Multiple object at one time or a id


class NoteSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Note

        fields = ["id", "title", "content", "created_at", "author", "author_name"]
        extra_kwargs = {"author": {"read_only": True}}

    def validate(self, data):
        title = data.get("title")
        content = data.get("content")
        author = data.get("author")
        if (
            len(title) <= 5
            or len(title) >= 10
            or len(content) <= 5
            or len(content) >= 40
        ):
            raise serializers.ValidationError(
                "Title must be less than 10 and  greator than 5  while content must be less than 40 and greator than 5"
            )
        return data  # for all once validation system
