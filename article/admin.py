from django.contrib import admin
from article.models import Article, Comment, Category

# Register your models here.

#admin.site.register(Article) # (Article, ArticleAdmin)

#---> ADMİN PANELİ ÖZELLEŞTİRMELERİ <---#
admin.site.register(Comment)
admin.site.register(Category)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_date"]
    list_display_links = ["title", "author", "created_date"]
    search_fields = ["title"] # Arama Alanı
    list_filter = ["created_date"] # oluşturulma tarihine göre filter seçeneği
    #date_hierarchy = 'created_date'
    #empty_value_display = '-empty-'

    class Meta:
        model = Article
