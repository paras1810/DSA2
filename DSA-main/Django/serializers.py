from datetime import datetime
from rest_framework import serializers

class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created

comment = Comment("abc@gmail.com", "foo-bar")

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)


class CommentSerializer(serializers.Serializer):
    user = UserSerializer(required=False)
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment(**validated_data)
        return Comment.objects.create(**validated_data) #If Django model instance
    
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.data = validated_data.get('data', instance.data)
        instance.created = validated_data.get('created', instance.created)
        instance.save() #If Django model instance
        return instance


serializer = CommentSerializer(comment)
serializer.data

def mulitple_of_10(value):
    if value%10!=0:
        raise serializers.ValidationError('Not a multiple of 10')
    

class EventSerializer(serializers.Serializer):
    desc = serializers.CharField(max_length=50)
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()
    score = serializers.IntegerField(validators = [mulitple_of_10])

    def validate_desc(self, value):
        if 'Django' not in value.lower():
            raise serializers.ValidationError("Not about Django")
        return value
    
    def validate(self, data):
        if data['start'] > data['finish']:
            raise serializers.ValidationError("finish before start")
        return data
    
class AerodromeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aerodrome
        fields = ['name', 'Longitude', 'Latitude']
        #fields = __all__, exclude = ['users'], read_only_fields = ['account_name']
    







