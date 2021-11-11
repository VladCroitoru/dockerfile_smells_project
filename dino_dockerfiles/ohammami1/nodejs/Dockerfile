FROM node:6.13.1-stretch 

RUN apt-get update

ARG user=node

ADD entrypoint.sh /usr/bin/entrypoint.sh
RUN chmod +x /usr/bin/entrypoint.sh

RUN mkdir -p /website

USER ${user}

ENTRYPOINT ["/usr/bin/entrypoint.sh"]

WORKDIR "/website"

