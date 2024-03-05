import os

from django.apps import apps
from django.conf import settings
from django.core.asgi import get_asgi_application
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "encost.settings")

apps.populate(settings.INSTALLED_APPS)

# импорт должен быть размещен именнно под populate, иначе ошибка
from fast_api.api_router import router as api_router


def get_application() -> FastAPI:

    app = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        debug=settings.DEBUG
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin) for origin in settings.ALLOWED_HOSTS] or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router, prefix=settings.API_V1_STR)
    app.mount("/django", get_asgi_application())
    return app


app = get_application()
