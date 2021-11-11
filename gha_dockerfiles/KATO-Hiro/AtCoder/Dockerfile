# See:
# https://hub.docker.com/_/python
FROM python:3.8-alpine

WORKDIR /usr/src/app

# See:
# https://qiita.com/ryuichi1208/items/6020cfabc92bd8153654
# https://github.com/alpine-docker/git/issues/1
# http://orolog.hatenablog.jp/entry/2018/09/03/233609
RUN apk update && apk --no-cache add openssh gcc fish git libc-dev libxml2-dev libxslt-dev

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
