FROM fpco/stack-run
MAINTAINER Pascal Hartig <phartig@rdrei.net>

ARG PROGVERSION=v0.1.3.0

RUN apt-get install -y curl && mkdir -p /srv
RUN curl -L https://github.com/passy/disruption-tracker/releases/download/$PROGVERSION/disruption-tracker.lnx64.tar.bz2 | tar -C /srv -xjvf - disruption-tracker

WORKDIR /srv
ENTRYPOINT ["/srv/disruption-tracker"]

# vim:tw=0:
