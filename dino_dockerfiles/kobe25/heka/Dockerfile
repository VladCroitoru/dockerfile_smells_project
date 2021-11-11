FROM debian:8
MAINTAINER Antonio Esposito "kobe@befair.it"

COPY heka.deb /tmp/heka.deb
RUN dpkg -i /tmp/heka.deb

COPY conf /etc/hekad

CMD ["hekad", "--config", "/etc/hekad"]
