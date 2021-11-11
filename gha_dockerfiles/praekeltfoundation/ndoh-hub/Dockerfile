FROM praekeltfoundation/django-bootstrap:py2

COPY . /app
RUN pip install -e .

ENV DJANGO_SETTINGS_MODULE "ndoh_hub.settings"
RUN ./manage.py collectstatic --noinput
CMD ["ndoh_hub.wsgi:application"]
