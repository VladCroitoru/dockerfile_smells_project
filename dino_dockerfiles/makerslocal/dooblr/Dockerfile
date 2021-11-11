FROM python:2-alpine

RUN apk update && apk upgrade && \
    apk add --no-cache git

COPY . /dooblr

WORKDIR /dooblr

RUN git fetch --unshallow && git fetch --tags && pip install ./ 

ENTRYPOINT ["dooblr"]
