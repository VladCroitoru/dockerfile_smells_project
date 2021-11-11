FROM ubuntu:14.04
MAINTAINER Steve Mayne <steve.mayne@gmail.com>

RUN apt-get update -y && apt-get install -q -y \
	make "g++" git-core libqt4-webkit libqt4-dev libgl1-mesa-dri python-imaging qt4-qmake x11-xkb-utils xfonts-75dpi xfonts-100dpi xfonts-cyrillic xfonts-scalable xserver-xorg-core xvfb

RUN git clone https://github.com/marazmiki/CutyCapt.git /tmp/CutyCapt

WORKDIR /tmp/CutyCapt
RUN qmake && make

# Put the CutyCapt binary into /usr/bin
RUN cp /tmp/CutyCapt/CutyCapt /usr/bin/cutycapt

RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir /thumbnails
VOLUME /thumbnails

RUN mkdir -p /etc/opt/
ADD conf/thumbnailsvc.cfg /etc/opt/thumbnailsvc.cfg
RUN chown root.root /etc/opt/thumbnailsvc.cfg && chmod 644 /etc/opt/thumbnailsvc.cfg

RUN mkdir -p /opt/thumbnailsvc
ADD src/ /opt/thumbnailsvc
RUN chmod +x /opt/thumbnailsvc/thumbnailsvc.py

WORKDIR /opt/thumbnailsvc/
EXPOSE 8080

CMD ["/opt/thumbnailsvc/thumbnailsvc.py"]