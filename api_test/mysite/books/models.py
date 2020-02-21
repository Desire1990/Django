from django.db import models

class Book(models.Model):
    COVER = 1
    PAPER = 2
    EBOOK = 3
    BOOK_TYPES = (
        (COVER, 'cover'), 
        (PAPER, 'Paper'),
        (EBOOK, 'E-book'),
    )

    title       = models.CharField(max_length=200,
                                     unique=True)
    slug        = models.SlugField(max_length=200, 
                                    unique=True)
    author      = models.CharField(max_length=30,
                                   blank=True)
    content     = models.TextField()
    # picture     = models.ImageField()
    updated_on  = models.DateTimeField(auto_now= True)
    created_on  = models.DateField(auto_now= True,
                                        blank=True,
                                        null=True)
    
    price       = models.DecimalField(max_digits=5, decimal_places=2)
    pages       = models.IntegerField(blank=True, null=True)
    book_type   = models.PositiveSmallIntegerField(choices=BOOK_TYPES,
                                                 blank=True, 
                                                 null=True)