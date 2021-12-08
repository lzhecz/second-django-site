from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import News, Category


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id',
                    'title',
                    'category',
                    'slug',
                    'time_create',
                    'time_update',
                    'get_photo',
                    'is_published',
                    )
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published')
    fields = ('title',
              'category',
              'content',
              'photo',
              'get_photo',
              'is_published',
              'time_create',
              'time_update',
              )
    readonly_fields = ('get_photo', 'time_create', 'time_update', )
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<a href='{obj.photo.url}'><img src='{obj.photo.url}' width=50></a>")

    get_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'title',
                    'slug',
                    )
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'
