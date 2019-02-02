from django.db import models

from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete= models.CASCADE, verbose_name="Kullanıcı")
    # on_delete= models.CASCADE -> user silindiği zaman user ile ilgili makale vb silinsin
    title = models.CharField(max_length=50, verbose_name="Başlık")
    category = models.ForeignKey('Category', verbose_name='Kategori', on_delete=models.CASCADE, null=True, blank=True)
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    article_image = models.ImageField(blank=True, null=True, verbose_name="Makaleye Fotoğraf Ekleyin")
    views = models.PositiveIntegerField(default=0)
 


    def __str__(self):
        return self.title

    #class Meta:
    #    ordering = ['-created_date']

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Makale", related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="İsim")
    comment_content = models.CharField(max_length=200, verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True, verbose_name="Yorum Tarihi")

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']

class Category(models.Model):
    category_name = models.CharField(max_length=25, verbose_name="Kategori İsmi")

    def __str__(self):
        return self.category_name
