FROM python:3-alpine

MAINTAINER Hemang S Kumar <hemangsk@gmail.com>

RUN mkdir -p /bot

WORKDIR /bot

COPY ./requirements.txt /bot

RUN pip install -r requirements.txt

RUN apk update && apk upgrade && \
    apk add --no-cache bash git

RUN git clone --depth 1 https://github.com/coala/coala-quickstart.git \
&& time pip3 install --no-cache-dir -e coala-quickstart

COPY . /bot

CMD ["python3", "coafile_bot.py"]

