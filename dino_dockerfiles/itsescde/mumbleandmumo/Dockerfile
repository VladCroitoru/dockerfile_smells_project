FROM ubuntu:16.04
MAINTAINER ITSESCDE <schuetz@itsesc.ovh>

RUN useradd -u 1000 mumble \
 && apt-get update \
 && apt-get install -y mumble-server python git python-zeroc-ice \
 && mkdir /data && chown 1000 /data
 

ADD mumble-server.ini /mumble-server.ini

RUN git clone https://github.com/mumble-voip/mumo.git

ADD mumo.ini /mumo/mumo.ini

CMD python mumo.py -d

VOLUME ["/data", "/config"]
EXPOSE 64738/udp

USER mumble
ENTRYPOINT ["/usr/sbin/murmurd", "-fg", "-ini", "/config/mumble-server.ini"]
