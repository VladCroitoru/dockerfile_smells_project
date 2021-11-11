FROM debian:jessie

# GENERAL DEPENDENCIES
RUN apt-get update && \
    apt-get -y install curl

# 
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" | tee -a /etc/apt/sources.list.d/jessie-backports.list
RUN apt-get update

# Pip
RUN apt-get -y install python-pip

# Gunicorn
RUN apt-get update
RUN pip install gunicorn

# Flask
RUN apt-get -y install python-dev
RUN pip install Flask

# Cron
RUN apt-get -y install cron
ADD docker/crontab /app/crontab
RUN crontab /app/crontab

# Project env and files
ENV PROJECT_HOME /Preco
RUN mkdir /Preco
RUN mkdir /Preco/src
RUN mkdir /Preco/data
COPY src /Preco/src/
COPY data /Preco/data/
COPY README.md /Preco/
RUN chmod u+x /Preco/src/main/script/autostart.sh

# Snowplow python tracker
RUN pip install snowplow-tracker

# Fix requests
RUN easy_install --upgrade pip
RUN pip install requests==2.6.0

# Kafka support
RUN pip install kafka

ENTRYPOINT ["/Preco/src/main/script/autostart.sh"]
