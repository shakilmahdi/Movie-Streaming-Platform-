from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review



# def name_length( value):
#         if len(value)<2:
#             raise serializers.ValidationError("Name must be at least 2 characters long")

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model= Review
        exclude =('watchlist',)
        # fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = "__all__"
        # # fields = ['id', 'name', 'description', 'active']
        # exclude = ['name', 'description']

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many = True, read_only = True)
    # watchlist = serializers.StringRelatedField(many= True)
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='movie-detail',
        
    # )
    
    class Meta:
        model = StreamPlatform
        fields = '__all__' 
         
          
# class StreamPlatformSerializer(serializers.ModelSerializer):
#     watchlist = WatchListSerializer(many=True, read_only=True)

#     class Meta:
#         model = StreamPlatform
#         fields = "__all__"
        
        
        
        
        
        
        
    # def get_len_name(self, object): 
    #     return len(object.name)
    
        
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Title and description cannot be the same")
    #     return data
        
    # def validate_name(self, value):
    #     if len(value)<2:
    #         raise serializers.ValidationError("Name must be at least 2 characters long")
    #     else:
    #         return value  
        
    #     id = serializers.IntegerField(read_only=True)
#     name= serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField() 
 
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and description cannot be the same")
#         return data 