FROM ubuntu:latest

RUN apt-get update -y && apt-get install -y gcc pkg-config make libmicrohttpd-dev

RUN mkdir -p /tmp/tempsite
COPY . /tmp/tempsite

RUN cd /tmp/tempsite && ./configure && make install

EXPOSE 8080

CMD ("/usr/local/bin/stuph_temp_httpd")

