# FROM ethereum/client-go:release-1.8
FROM ethereum/client-go:v1.8.27
USER root
ADD . /usr/src/app
WORKDIR /usr/src/app

ENV LANG C.UTF-8
RUN apk add --no-cache ca-certificates python3 python3-dev gcc linux-headers libc-dev bash curl
RUN pip3 install --upgrade pip
RUN pip3 install -U setuptools

RUN pip3 install -r requirements.txt
