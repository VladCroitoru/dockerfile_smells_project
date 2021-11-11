FROM alpine

MAINTAINER Jonathan Baldie "jon@jonbaldie.com"

ADD install.sh install.sh
RUN chmod +x install.sh && sh install.sh && rm install.sh

WORKDIR "/app"
VOLUME ["/app"]

CMD ["/root/.yarn/bin/yarn"]
