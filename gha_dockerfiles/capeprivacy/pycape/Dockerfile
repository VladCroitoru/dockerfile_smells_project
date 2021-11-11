FROM python:3.8-slim-buster

RUN apt-get update     && \
    apt-get install -y    \
        ca-certificates make

WORKDIR /pycape

COPY . ./

RUN make bootstrap

ENTRYPOINT [ "poetry" ]
