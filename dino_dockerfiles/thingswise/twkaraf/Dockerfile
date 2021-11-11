FROM java:8
MAINTAINER Alexander Lukichev
EXPOSE 5000

VOLUME /cfg

VOLUME /app

ADD https://github.com/Yelp/dumb-init/releases/download/v0.5.0/dumb-init_0.5.0_amd64 /dumb-init

ADD runkaraf.sh /
RUN chmod +x /runkaraf.sh /dumb-init

WORKDIR /app

ENTRYPOINT ["/runkaraf.sh"]

