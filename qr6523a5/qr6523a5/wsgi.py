import os
import sys

# Layihənin əsas qovluğunu əlavə edin
project_home = 'qr6523a5/qr6523a5'  # Əsas layihə qovluğunuz
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Virtual mühiti aktivləşdirin (əgər varsa)
activate_this = 'myvenv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Django layihəsinin settings faylını göstərin
os.environ['DJANGO_SETTINGS_MODULE'] = 'qr6523a5.settings'  # Layihə adını uyğunlaşdırın

# Django WSGI tətbiqini yaradın
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
