from __future__ import absolute_import, unicode_literals

from myapp.celery import celery as celery_app
from myapp.controllers import base_bp  # noqa F401
from myapp.models import User  # noqa F401


__all__ = ["celery_app"]
