from django.contrib import admin
from .models import Contact,Category,Type,Items,Cart,User,Account,Billing,Payment

# Register your models here.
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Type)
admin.site.register(Items)
admin.site.register(Cart)
admin.site.register(User)
admin.site.register(Account)
admin.site.register(Billing)
admin.site.register(Payment)
