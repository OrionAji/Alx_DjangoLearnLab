from rest_framework import serializers
from .models import Arthur, Book
import datetime

class ArthurSerializer(serializers.ModelSerializer):
   
   # Serializes the Arthur model, ensuring all fields are serialized. 
   # Includes custom validation for publication_year. 
    
    class Meta:
        model = Arthur
        fields = '__all__'
        
    def validate_publication_year(self, value):
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class BookSerializer(serializers.ModelSerializer):
    # Serializes the Book model, ensuring all fields are serialized. 
    # Includes custom validation for publication_year.
    book = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
