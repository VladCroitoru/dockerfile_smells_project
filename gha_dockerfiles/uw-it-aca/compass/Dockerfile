FROM gcr.io/uwit-mci-axdd/django-container:1.3.1 as app-prewebpack-container

# Choose one database connector for MCI
#USER root
#RUN apt-get update && apt-get install libpq-dev -y
#RUN apt-get update && apt-get install mysql-client libmysqlclient-dev -y
USER acait

ADD --chown=acait:acait app_name/VERSION /app/app_name/
ADD --chown=acait:acait setup.py /app/
ADD --chown=acait:acait requirements.txt /app/

RUN . /app/bin/activate && pip install -r requirements.txt
# Match db connector to your chosen DB
#RUN . /app/bin/activate && pip install mysqlclient
#RUN . /app/bin/activate && pip install psycopg2

FROM node:14.6.0-stretch AS wpack

ADD ./package.json /app/
WORKDIR /app/
RUN npm install .

ADD . /app/

ARG VUE_DEVTOOLS
ENV VUE_DEVTOOLS=$VUE_DEVTOOLS
RUN npx webpack --mode=production

FROM app-prewebpack-container as app-container

COPY --chown=acait:acait --from=wpack /static /static

ADD --chown=acait:acait . /app/
ADD --chown=acait:acait docker/ project/

RUN . /app/bin/activate && python manage.py collectstatic --noinput

FROM gcr.io/uwit-mci-axdd/django-test-container:1.3.1 as app-test-container

ENV NODE_PATH=/app/lib/node_modules
COPY --from=app-container /app/ /app/
COPY --from=app-container /static/ /static/
