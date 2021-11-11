FROM java:8
MAINTAINER Alexander Lukichev
EXPOSE 5000

VOLUME /app

ADD https://github.com/Yelp/dumb-init/releases/download/v0.5.0/dumb-init_0.5.0_amd64 /dumb-init

ADD runjava.sh /
RUN chmod +x /runjava.sh /dumb-init

WORKDIR /app

ENTRYPOINT ["/runjava.sh"]

