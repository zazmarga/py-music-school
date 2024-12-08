from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):

    class Meta:
        model = Musician
        fields = (
            "id",
            "first_name",
            "last_name",
            "instrument",
            "age",
            "date_of_applying",
            "is_adult",
        )

    def validate_age(self, age):
        if age < 14:
            raise serializers.ValidationError(
                "Age must be at least 14 years old"
            )
        return age
