FROM python:3

RUN apt-get update && apt-get install -y gettext-base nginx && apt-get clean
RUN unlink /etc/nginx/sites-enabled/default
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./docker/config/nginx.conf.template /opt/
COPY ./docker/config/vhost.conf.template /opt/

COPY ./extra/legacy_migration.py /
COPY ./shoppingList/shoppingList/settings.py /local.py.template
COPY ./shoppingList /shoppingList
COPY ./docker/entrypoint /entrypoint

ENTRYPOINT ["/entrypoint"]

