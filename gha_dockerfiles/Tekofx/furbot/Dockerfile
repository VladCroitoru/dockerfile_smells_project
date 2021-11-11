FROM python:3.8-slim-buster

WORKDIR /bot/
COPY requirements.txt /tmp/
ENV TZ="Europe/Madrid"
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential libffi-dev  \
        libtiff-dev libfreetype6-dev \
        libwebp-dev \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/* \
        && pip3 install -r /tmp/requirements.txt --no-cache-dir \
        && rm /tmp/requirements.txt 

CMD [ "python3","/bot/src/main.py" ]
