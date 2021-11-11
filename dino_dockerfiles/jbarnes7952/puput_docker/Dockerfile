FROM python:latest

RUN apt-get update && \
	apt-get install -y vim expect
RUN pip install wagtail wagtailcodeblock psycopg2 django-el-pagination gunicorn graphene-django
RUN git clone git://github.com/jbarnes7952/puput /puput_src
WORKDIR /app
RUN wagtail start blog
RUN cp -r /puput_src/puput /app/blog
COPY blog/settings/base.py /app/blog/blog/settings/base.py
COPY blog/urls.py /app/blog/blog/urls.py
COPY puput-patch/load_data.sh /app/blog
COPY puput-patch/my_migrate.exp /app/blog 
COPY datadump.json /app/blog

WORKDIR /app/blog
COPY api api
EXPOSE 80
