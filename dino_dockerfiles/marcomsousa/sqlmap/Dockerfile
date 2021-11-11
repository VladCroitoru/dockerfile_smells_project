FROM python:2.7-alpine
MAINTAINER Marco Sousa <marcomsousa+docker @ gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apk update && apk upgrade && \
    apk add --no-cache git

RUN git clone https://github.com/sqlmapproject/sqlmap.git

WORKDIR /sqlmap
VOLUME /data

CMD ["-version"]
ENTRYPOINT ["./sqlmap.py"]
