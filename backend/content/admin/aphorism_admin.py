from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from django_summernote.admin import SummernoteModelAdmin

from content.models import Aphorism


@admin.register(Aphorism)
class AphorismAdmin(TabbedTranslationAdmin, SummernoteModelAdmin):
    list_display = ('id', 'get_small_text',)
    list_display_links = ('get_small_text',)
    summernote_fields = ('text',)

    def get_small_text(self, object):
        return f'{object.text[:67]}...' if len(object.text) > 70 else object.text

    get_small_text.short_description = ""
