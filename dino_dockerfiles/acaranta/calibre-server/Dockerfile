FROM ubuntu:14.04
MAINTAINER arthur@caranta.com


RUN apt-get update -y && apt-get dist-upgrade -y
RUN apt-get install -y python wget git xz-utils imagemagick
RUN rm /tmp/calibre* -Rf 2>&1 >/dev/null && wget -nv -O- https://raw.githubusercontent.com/kovidgoyal/calibre/master/setup/linux-installer.py | sudo python -c "import sys; main=lambda:sys.stderr.write('Download failed\n'); exec(sys.stdin.read()); main()"
WORKDIR /opt/calibre

RUN mkdir -p /calibre-lib

VOLUME ["/calibre-lib"]
EXPOSE 8080
ENV USER calibre
ENV PASS calibre

CMD /opt/calibre/calibre-server --with-library=/calibre-lib --username=$USER --password=$PASS


