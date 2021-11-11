
FROM perljedi/dzil_docker:latest
MAINTAINER Dave Mueller <dave@perljedi.com>

ADD . /opt/docker-web-interface
WORKDIR /opt/docker-web-interface
RUN cpanm --quiet --notest Twiggy
RUN dzil authordeps --missing | cpanm --quiet --notest
RUN dzil install

EXPOSE 9999

CMD ["/bin/sh", "-c", "twiggy --port 9999 -D"]
