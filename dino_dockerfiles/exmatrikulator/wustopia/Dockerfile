FROM alpine

# expose web server port
# only http, for ssl use reverse proxy
EXPOSE 80

#build tools for Flask-SQLAlchemy-->cffi
RUN apk add --no-cache bash git nginx uwsgi uwsgi-python3 python3-dev libffi-dev alpine-sdk postgresql-dev graphviz ttf-dejavu jpeg-dev zlib-dev\
	&& pip3 install --upgrade pip


# application folder
ENV APP_DIR /app
VOLUME [ "/app/migrations", "/app/config" ]

# app dir
COPY webapp ${APP_DIR}/webapp
COPY .git/HEAD ${APP_DIR}/version.txt
COPY app.ini app.py babel.cfg config.py.example entrypoint.sh manage.py requirements.txt tests.py worker.py ${APP_DIR}/
COPY nginx.conf /etc/nginx/nginx.conf
RUN chmod 777 -R /run/
WORKDIR ${APP_DIR}

RUN pip3 install -r requirements.txt
RUN python3 manage.py pybabel_compile

# exectute start up script
ENTRYPOINT ["/app/entrypoint.sh"]
