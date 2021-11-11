FROM ubuntu:15.04

RUN set -ex; \
    apt-get update -qq; \
    apt-get -y install \
      ffmpeg \
      git \
      imagemagick \
      libopencv-dev \
      libpq-dev \
      ocl-icd-opencl-dev \
      python-dev \
      python-opencv \
      python-pip \
      virtualenv \
    ; \
    rm -rf /var/lib/apt/lists/*

RUN pip install git+git://github.com/aanand/butterflow.git@e51d8ea5675ac80b335bc1c9caef7997364b759b

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

ADD . /code

ENV PYTHONUNBUFFERED 1
CMD ["python", "bot.py"]
