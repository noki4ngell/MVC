from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_year(value):
    current_year = timezone.now().year
    if value < 1000 or value > current_year:
        raise ValidationError(f"Rok wydania musi być między 1000 a {current_year}.")

class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Imię")
    last_name = models.CharField(max_length=100, verbose_name="Nazwisko")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tytuł")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Autor")
    year = models.IntegerField(validators=[validate_year], verbose_name="Rok wydania")

    def __str__(self):
        return self.title

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Książka")
    borrower_name = models.CharField(max_length=150, verbose_name="Kto wypożyczył")
    loan_date = models.DateField(auto_now_add=True, verbose_name="Data wypożyczenia")
    return_date = models.DateField(null=True, blank=True, verbose_name="Data zwrotu")

    def __str__(self):
        return f"{self.book.title} - {self.borrower_name}"