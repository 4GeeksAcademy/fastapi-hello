from fastapi import FastAPI
from .admin import site
from .utils import apply_basic_configuration, include_routers

# Start a new API
app = FastAPI()

# Basic config including CORS, error handlers and sitemap
app = apply_basic_configuration(app)

# Include all the routers from the routers folder
app = include_routers(app)

# Add the admin panel to manage the database info and the users
site.mount_app(app)