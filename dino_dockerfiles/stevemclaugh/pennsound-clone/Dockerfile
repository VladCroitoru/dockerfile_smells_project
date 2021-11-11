# Audio Labeling Container
FROM ubuntu:14.04

MAINTAINER Steve McLaughlin <stephen.mclaughlin@utexas.edu>

EXPOSE 3805

ENV SHELL /bin/bash
ENV PYTHONWARNINGS="ignore:a true SSLContext object"

# Update OS
RUN apt-get update && apt-get install -y \
software-properties-common \
build-essential \
python-dev \
python-pip \
wget \
git \
unzip \
dpkg \
gunicorn \
libxml2-dev \
libxslt1-dev \
libssl-dev \
&& python -m pip install -U pip

COPY ./setup.sh /var/local/

COPY ./requirements.txt /var/local/
RUN pip install -qr /var/local/requirements.txt

RUN mkdir -p /home/PennSound_pages/
COPY ./PennSound_pages/ /home/PennSound_pages/

RUN mkdir -p /home/static/
COPY ./static/ /home/static/

RUN mkdir -p /home/templates/
COPY ./templates/ /home/templates/

COPY ./PennSound_metadata.csv /home/
COPY ./app.py /home/
COPY ./wsgi.py /home/
COPY ./load_metadata_db.py /home/

# Install FFmpeg with mp3 support
#RUN add-apt-repository -y ppa:mc3man/trusty-media \
# && apt-get update -y \
# && apt-get install -y ffmpeg gstreamer0.10-ffmpeg

WORKDIR /home/
CMD ["bash","/var/local/setup.sh"]
