FROM node:4.6.0
MAINTAINER Alexander Lukichev
EXPOSE 5000

VOLUME /app

ADD https://github.com/Yelp/dumb-init/releases/download/v0.5.0/dumb-init_0.5.0_amd64 /dumb-init

ADD runnode.sh /
RUN chmod +x /runnode.sh /dumb-init

WORKDIR /app

ENTRYPOINT ["/runnode.sh"]

