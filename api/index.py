import os
import sys
from django.core.wsgi import get_wsgi_application

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

app = get_wsgi_application()
