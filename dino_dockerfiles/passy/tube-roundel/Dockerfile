FROM fpco/stack-run
MAINTAINER Pascal Hartig <phartig@rdrei.net>

ARG PROGVERSION=v0.1.0.4

RUN apt-get install -y curl && mkdir -p /srv
RUN curl -L https://github.com/passy/tube-roundel/releases/download/$PROGVERSION/tube-roundel.lnx64.tar.bz2 | tar -C /srv -xjvf - tube-roundel

COPY res/* /srv/res/
WORKDIR /srv
EXPOSE 8080
ENTRYPOINT ["/srv/tube-roundel"]

# vim:tw=0:
