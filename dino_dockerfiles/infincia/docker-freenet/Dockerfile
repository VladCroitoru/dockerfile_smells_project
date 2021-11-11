FROM java:openjdk-8-jre-alpine

MAINTAINER Stephen Oliver <steve@infincia.com>

ADD ./fred/* /fred/

ADD ./defaults/freenet.ini /defaults/

VOLUME ["/conf", "/data"]

# expose port(s)
EXPOSE 8888
EXPOSE 9481

WORKDIR /fred

CMD /fred/docker-run
