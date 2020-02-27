from django.urls import path
from . views import (
					BookListAPIView,
					BookCreateAPIView, 
					BookUpdateAPIView, 
					BookDetailAPIView,
					BookDeleteAPIView)
app_name = 'books'

urlpatterns =[
	path('books/', BookListAPIView.as_view(), name = 'list'),
	path('books/create', BookCreateAPIView.as_view(), name = 'create'),
	path('books/<pk>/detail', BookDetailAPIView.as_view(), name = 'detail'),
	path('books/<pk>/edit', BookUpdateAPIView.as_view(), name = 'update'),
	path('books/<pk>/delete', BookDeleteAPIView.as_view(), name = 'delete'),
]