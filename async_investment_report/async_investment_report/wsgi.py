import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'async_investment_report.settings')
application = get_wsgi_application()
