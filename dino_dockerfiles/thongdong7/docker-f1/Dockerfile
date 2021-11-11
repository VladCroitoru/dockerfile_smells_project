FROM tiangolo/uwsgi-nginx:python2.7

# Add app configuration to Nginx
COPY nginx.conf /etc/nginx/conf.d/
COPY entrypoint.sh /app/entrypoint.sh
COPY uwsgi.ini /app/uwsgi.ini

RUN pip install \
    awscli \
    backports-abc==0.4 \
    boto3==1.4.3 \
    certifi==2016.8.31 \
    click==6.6 \
    enum34==1.1.6 \
    flask-cors==3.0.2 \
    Flask-Login==0.3.2 \
    Flask-Script==2.0.5 \
    Flask-SQLAlchemy==2.1 \
    flask-stormpath==0.4.8 \
    Flask-Testing==0.6.1 \
    Flask==0.11.1 \
    future==0.15.2 \
    futures==3.0.5 \
    itsdangerous==0.24 \
    Jinja2==2.8 \
    json5==0.2.4 \
    MarkupSafe==0.23 \
    msgpack-python==0.4.8 \
    MySQL-python==1.2.5 \
    pycrypto==2.6.1 \
    PyFunctional==1.0.0 \
    PyMySQL==0.7.9 \
    python-dateutil==2.5.3 \
    pytz==2016.6.1 \
    PyYAML==3.12 \
    redis==2.10.5 \
    requests==2.11.1 \
    ruamel.yaml==0.13.14 \
    simplejson==3.8.2 \
    singledispatch==3.4.0.3 \
    six==1.10.0 \
    SQLAlchemy==1.1.4 \
    tb-ioc==0.3.4 \
    warrant==0.2.0 \
    Werkzeug==0.11.11

RUN apt-get update && apt-get install -qqy unzip

#ENTRYPOINT ["bash", "/app/entrypoint.sh"]
