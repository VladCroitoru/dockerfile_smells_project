FROM praekeltfoundation/django-bootstrap:py2

ENV DJANGO_SETTINGS_MODULE=thandibot.production

RUN pip install "Django>=1.9,<1.10" "djangorestframework<4.0" "psycopg2<3.0"

COPY . /app
RUN pip install -e .

RUN django-admin collectstatic --noinput

CMD ["thandi.wsgi:application", "--timeout", "1800"]
