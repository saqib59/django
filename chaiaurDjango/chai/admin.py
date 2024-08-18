from django.contrib import admin
from .models import ChaiVarity, ChaiReview, Store, ChaiCertificate

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2

class ChaiVariertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'chai_type', 'date_added')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties',)


class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number')

admin.site.register(ChaiVarity, ChaiVariertyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
