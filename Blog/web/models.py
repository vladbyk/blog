from django.db import models

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15,verbose_name='NameAutor')
    age = models.IntegerField(verbose_name='AgeAutor')
    sex = models.CharField(max_length=10,choices=(("W","Women"),("M","Men")))


    def __str__(self):
        return f"{self.author_id} | {self.name}"


    class Meta :
       verbose_name = "Authors"
       verbose_name_plural = "AuthorsES"
       ordering = ('author_id',)

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15,verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    author = models.ForeignKey(Author,on_delete=models.CASCADE,verbose_name="Автор")
    #author = models.ManyToManyField(Author)
    img = models.CharField(max_length=150,verbose_name="Путь к изображению")

    def __str__(self):
        return str(self.name)

    class Meta :
       verbose_name = "Книга"
       verbose_name_plural = "Книги"
       ordering = ('book_id',)

