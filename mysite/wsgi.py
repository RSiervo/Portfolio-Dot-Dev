import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

# Django’s WSGI app
application = get_wsgi_application()

# Vercel requires this
app = application
handler = application  # alias for compatibility
