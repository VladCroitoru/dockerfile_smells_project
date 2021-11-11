## Set the base image to Ubuntu ##
FROM ubuntu:14.04
ARG DEBIAN_FRONTEND=noninteractive
 
## File Author / Maintainer ##
MAINTAINER chvb
 
## Install ##
RUN apt-get update && apt-get install -y wget cryptsetup dnsutils resolvconf sysstat lsof openssh-server supervisor krb5-kdc krb5-admin-server && \
    mv /etc/krb5.conf /opt/kerio && ln -sf /opt/kerio/krb5.conf /etc/krb5.conf
RUN wget -O kerio-connect-linux-64bit.deb http://download.kerio.com/dwn/kerio-connect-linux-64bit.deb && \
    dpkg -i kerio-connect-linux-64bit.deb && apt-get install -f && rm -f kerio-connect-linux-64bit.deb

## Clean ##
RUN apt-get clean && \
    apt-get autoclean && \
    apt-get autoremove -y && \
    rm -rf /build && \
    rm -rf /tmp/* /var/tmp/* && \
    rm -rf /var/lib/apt/lists/* && \
    rm -f /etc/dpkg/dpkg.cfg.d/02apt-speedup

## set up openssh server and supervisord ##
RUN mkdir -p /var/log/supervisord
RUN mkdir -p /var/run/sshd
RUN locale-gen en_US.utf8
RUN useradd docker -d /home/docker -g users -G sudo -m                                                                                                                    
RUN echo docker:test123 | chpasswd
ADD /etc/supervisor/conf.d/supervisord.conf /etc/supervisor/conf.d/supervisord.conf 

## Kerio Connect start script ##
ADD /etc/init.d/kerio-connect.sh /etc/init.d/kerio-connect.sh
RUN chmod +x /etc/init.d/kerio-connect.sh

## Prepare start ##
RUN mkdir /opt-start && mv /opt/kerio /opt-start

## Expose the default portonly 4040 is nessecary for admin access ##
EXPOSE 4040 22 25 465 587 110 995 143 993 119 563 389 636 80 443 5222 5223 
 
## Expose Volumes ## 
VOLUME /backup
VOLUME /mailserver/data 
VOLUME /opt/kerio

## Set default container command ##
ENTRYPOINT ["/usr/bin/supervisord"]
CMD ["-c", "/etc/supervisor/conf.d/supervisord.conf"] 
