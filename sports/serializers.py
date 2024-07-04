from rest_framework import serializers
from .models import Sport, SportImage

class SportImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportImage
        fields = ['image']

class SportSerializer(serializers.ModelSerializer):
    images = SportImageSerializer(many=True)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Sport
        fields = ['id', 'title', 'description', 'author', 'images']

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        sport = Sport.objects.create(**validated_data)
        for image_data in images_data:
            SportImage.objects.create(sport=sport, **image_data)
        return sport
