FROM python:3.7.4-buster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -qq 
RUN apt-get install -y libjpeg62-turbo libjpeg62-turbo-dev libfreetype6 libfreetype6-dev zlib1g-dev
RUN apt-get install -y libgeos-dev libgeos-3.7.1 libgeos-c1v5 gdal-bin gettext
RUN apt-get install -y locales -qq
RUN echo "pt_BR.UTF-8 UTF-8" >> /etc/locale.gen
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
RUN locale-gen
RUN dpkg-reconfigure locales
ENV LC_ALL=pt_BR.UTF-8
ENV LANG=pt_BR.UTF-8
ENV LANGUAGE=pt_BR.UTF-8
ENV LC_CTYPE=pt_BR.UTF-8
ENV LC_COLLATE=pt_BR.UTF-8

ENV GUNICORN_TIMEOUT 300
ENV GUNICORN_LOG_LEVEL info
ENV GUNICORN_WORKERS 2

ENV VERSION="$(git rev-parse --short HEAD)"

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 9090
RUN chmod +x /usr/src/app/docker-entrypoint.sh
CMD ["/usr/src/app/docker-entrypoint.sh"]
