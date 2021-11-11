FROM python:alpine
MAINTAINER Niklas Ekman (niklas.ekman@gmail.com)

ENV USERNAME="" \
    PASSWORD="" \
    CPANEL_HOST="freedns.oderland.com" \
    CPANEL_PORT="2083"

ADD internal_build.sh .
RUN ./internal_build.sh
WORKDIR /opt/cpanel-update-dns
ADD entrypoint.sh .

CMD ./entrypoint.sh
