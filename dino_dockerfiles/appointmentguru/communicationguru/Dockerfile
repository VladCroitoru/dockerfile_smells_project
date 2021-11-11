FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN echo 'APT::Default-Release "stable";' > /etc/apt/apt.conf
RUN mv /etc/apt/sources.list /etc/apt/sources.list.d/stable.list
RUN echo "deb http://ftp.debian.org/debian stretch main" > /etc/apt/sources.list.d/testing.list

# install all the dependencies except libcairo2 from jessie, then install libcairo2 from stretch
RUN apt-get -y update \
    && apt-get install -y \
        fonts-font-awesome \
        libffi-dev \
        libgdk-pixbuf2.0-0 \
        libpango1.0-0 \
        python-dev \
        python-lxml \
        shared-mime-info \
    && apt-get install -y libcairo2=1.14.8-1 \
    && apt-get -y clean

RUN mkdir -p /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -U pip
RUN pip install -r requirements.txt
ADD . /code/

