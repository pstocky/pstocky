# -*- coding:utf-8 -*-
import os
import sys
from os.path import abspath, dirname

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "base.settings")

project_dir = dirname(dirname(abspath(__file__)))
if project_dir not in sys.path:
    sys.path.append(project_dir)

application = get_wsgi_application()
