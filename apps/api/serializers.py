from rest_framework import serializers
from apps.api.models import Author

class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email']  # или можно прописать '__all__' если нужны все поля

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()

    def create(self, validated_data):
        """
        Создать и вернуть новый объект Author на основе предоставленных проверенных данных.
        """
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Обновить и вернуть существующий объект Author на основе предоставленных проверенных данных.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


