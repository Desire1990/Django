from rest_framework import serializers
from books.models import Book

# class BookSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Book
# 		fields = '__all__'



class BookListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ['id',
				  'title', 
				  'slug',
				  'author', 
				  'content', 
				  'created_on'
		]

class BookCreateUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ['title', 
				  # 'slug',
				  'author', 
				  'content', 
				  'price',
				  'created_on'

		]

class BookRetrieveSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ['title', 
				  'slug',
				  'author', 
				  'content', 
				  'created_on'
		]

class BookDestroySerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ['title', 
				  'slug',
				  'author', 
				  'content', 
				  'created_on'
		]

class BookUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ['title', 
				  'slug',
				  'author', 
				  'content', 
				  'created_on'
		]