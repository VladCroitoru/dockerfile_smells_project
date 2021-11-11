
FROM phusion/baseimage:0.9.11


MAINTAINER confucius68

RUN apt-get update && \
DEBIAN_FRONTEND=noninteractive apt-get install -y \
wget \
python \
xdg-utils \
ImageMagick && \
mkdir /opt/calibre

VOLUME ["/config"]

EXPOSE 8080

RUN cd /opt && \
wget --no-check-certificate -nv -O- https://raw.githubusercontent.com/kovidgoyal/calibre/master/setup/linux-installer.py | python -c "import sys; main=lambda:sys.stderr.write('Download failed\n'); exec(sys.stdin.read()); main('/opt/', True)"

CMD ["/opt/calibre/calibre-server","--with-library=/config","--username=$CALUSER","password=$CALPASSWORD"]
