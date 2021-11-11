FROM debian:jessie 

RUN apt-get update 
RUN apt-get install -y --no-install-recommends \ 
tftpd-hpa \ 
&& apt-get clean \ 
&& rm -rf /var/lib/apt/lists/*

RUN mkdir -p /srv/tftp 
ADD tftpd-hpa /etc/default/tftpd-hpa
VOLUME /srv/tftp 
RUN chmod -R 777 /srv/tftp && chown -R nobody /srv/tftp

EXPOSE 69/udp
ENTRYPOINT /etc/init.d/tftpd-hpa start && bash