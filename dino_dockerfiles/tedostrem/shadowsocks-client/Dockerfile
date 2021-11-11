FROM jreckner/docker-libsodium
MAINTAINER Ted Östrem <ted@t3d.one> 
RUN apt-get update && \
    apt-get install -y python-pip privoxy 
RUN pip install shadowsocks
RUN echo /usr/local/lib > /etc/ld.so.conf.d/usr_local_lib.conf && ldconfig
ADD config /etc/privoxy/config
ADD entrypoint.sh /root/entrypoint.sh
ENTRYPOINT ["/root/entrypoint.sh"]
