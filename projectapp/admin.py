from django.contrib import admin
from . models import Department,Doctors,Booking,Contact

# Register your models here.
admin.site.register(Department)
admin.site.register(Doctors)
# admin.site.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display=("id",'p_name','p_phone','p_mail','doc_name','booking_date','booked_on')
admin.site.register(Booking,BookingAdmin)
class ContactAdmin(admin.ModelAdmin):
    list_display=("id",'p_name','p_email','p_message','contact_on')
admin.site.register(Contact)