firebird

Для ручного коммита
from django.db import transaction
obj.save()
transaction.commit()

Или автокоммит в settings.py
'AUTOCOMMIT': True


django terminal
install ipython and django_extensions. django_extensions write settings.py
terminal
python manage.py shell_plus --print-sql
