from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from django_summernote.admin import SummernoteModelAdmin


from content.models import FAQ


@admin.register(FAQ)
class FAQAdmin(TabbedTranslationAdmin, SummernoteModelAdmin):
    list_display = ('id', 'question',)
    list_display_links = ('question',)
    
    search_fields = ('question',)
    summernote_fields = ('answer',)
