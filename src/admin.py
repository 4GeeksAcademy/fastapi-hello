import os
from fastapi_amis_admin import i18n
i18n.set_language(language='en_US')
from fastapi_amis_admin.admin.settings import Settings
from fastapi_amis_admin.admin.site import AdminSite
from fastapi_amis_admin.admin import admin
from .models import User
from .utils import add_documentation_panel

site = AdminSite(settings=Settings(database_url=os.getenv("DATABASE_URL")))
# We add the documentation to help students use the admin panel
site = add_documentation_panel(site)

""" 🔥 ⬇️ Add all your models below this line ⬇️ 🔥 """

# Adding this UserAdmin class will allow you to manage the User model from the admin panel
@site.register_admin
class UserAdmin(admin.ModelAdmin):
    page_schema = 'User'
    # set model
    model = User