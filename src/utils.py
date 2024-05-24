import os, importlib
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.routing import APIRoute
from fastapi_amis_admin.admin import admin
from fastapi_amis_admin.amis.components import PageSchema
from pydantic import ValidationError

class APIException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
    
def generate_sitemap(app: FastAPI):
    links = [{ "method": 'GET', "url": '/admin/', "params": None }]

    for route in app.routes:
        if isinstance(route, APIRoute):
            for method in route.methods:
                url = route.path
                links.append({ "method": method, "url": url, "params": route.dependant.path_params })

    links_html = ""
    for r in links:
        if r['params'] or r['method'] != "GET": links_html += f"<li>{r['method']} {r['url']}</li>"
        else: links_html += f"<li><a href='{r['url']}'>{r['method']} {r['url']}</a></li>"

    return f"""
        <div style="text-align: center;">
            <img style="max-height: 80px" src='https://storage.googleapis.com/breathecode/boilerplates/rigo-baby.jpeg' />
            <h1>Rigo welcomes you to your API!!</h1>
            <p>API HOST: <script>document.write('<input style="padding: 5px; width: 300px" type="text" value="'+window.location.href+'" />');</script></p>
            <p>Start working on your project by following the <a href="https://start.4geeksacademy.com/starters/flask" target="_blank">Quick Start</a></p>
            <p>Remember to specify a real endpoint path like: </p>
            <ul style="text-align: left;">{links_html}</ul>
        </div>
    """

def apply_basic_configuration(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Disable strict slashes
    for route in app.router.routes:
        if isinstance(route, APIRoute):
            route.strict_slashes = False


    @app.exception_handler(APIException)
    def api_exception_handler(request: Request, exc: APIException):
        return JSONResponse(
            status_code=exc.status_code,
            content=exc.to_dict(),
        )
    
    @app.exception_handler(ValidationError)
    def validation_exception_handler(request: Request, exc: ValidationError):
        print("Asdasdasd")
        errors = exc.errors()
        simplified_errors = [error['msg'] for error in errors]
        return JSONResponse(
            status_code=401,
            content={"message": simplified_errors}
        )
    
    @app.get("/")
    def read_root(request: Request):
        return HTMLResponse(generate_sitemap(app))
    
    # Create AdminSite instance
    return app

def add_documentation_panel(site):

    @site.register_admin
    class GitHubIframeAdmin(admin.IframeAdmin):
        page_schema = PageSchema(label='Documentation', icon='fa fa-github')
        src = 'https://4geeks.com/docs/start/react-flask-template'

    return site


def include_routers(app: FastAPI):
    routers_path = os.path.join(os.path.dirname(__file__), 'endpoints')
    for file in os.listdir(routers_path):
        if file.endswith('.py') and file != '__init__.py':
            module_name = file.replace('.py', '')
            module = importlib.import_module("src.endpoints."+module_name)
            app.include_router(module.router)

    return app
