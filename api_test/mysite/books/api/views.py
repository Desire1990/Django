# from rest_framework import generics
from rest_framework.generics import (ListAPIView,
										CreateAPIView, 
										RetrieveAPIView,
										UpdateAPIView, 
										DestroyAPIView								
									)
from ..models import Book
from .serializers import ( BookListSerializer, 
							BookDestroySerializer,		
							BookUpdateSerializer, 
							BookCreateUpdateSerializer,
							BookRetrieveSerializer
						)





# class BookListView(generics.ListAPIView): those comment lines are like theirs children
class BookListAPIView(ListAPIView):
	queryset = Book.objects.all()
	serializer_class = BookListSerializer



class BookCreateAPIView(CreateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookCreateUpdateSerializer
	# lookup_field = 'pk'


class BookDetailAPIView(RetrieveAPIView):
	queryset = Book.objects.all()
	serializer_class = BookRetrieveSerializer
	lookup_field = 'pk'


class BookUpdateAPIView(UpdateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookUpdateSerializer
	lookup_field = 'pk'

class BookDeleteAPIView(DestroyAPIView):
	queryset = Book.objects.all()
	serializer_class = BookDestroySerializer
	lookup_field = 'pk'